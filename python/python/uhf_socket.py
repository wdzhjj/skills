import time
import sys
import serial
import re
import requests
import configparser


class UHFSocket:

    def __init__(self, port, baudrate=115200, timeout=0.5):
        # 打开端口
        self.port = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        if not self.port.isOpen():
            print('连接串口失败')

    # 转成16进制的函数
    @staticmethod
    def convert_hex(string):
        result = []
        for i in string:
            result.append(hex(i))
        return result

    @staticmethod
    def check_sum(data):
        # 获取check_sum的值，在传自定义命令时使用，算出最后一位校验码
        if not isinstance(data, bytes):
            bytes.fromhex(data)
        u_sum = 0
        for i in range(len(data) // 2):
            u_sum += int(data[i * 2:i * 2 + 2], 16)
        u_sum = 256 - (u_sum % 256)
        return u_sum

    @staticmethod
    def parse_code(res, is_epc=False):
        if is_epc:  # 如果是epc值，说明是数据库表中取出的，直接按index进行取值
            tg_rcv_unit = res[0:16]  # 前16位为tg_rcv_unit
            tg_rcv_code_ox = res[16:19]  # 前17-19位为tg_rcv_code_ox
            tg_code_ox = res[19:24]  # 前20-24位为tg_code_ox
        else:  # 如果传过来的不是epc值，则说明是uhf设备读出来的值，需要进行处理
            _res = list(filter(None, res.split('0x')))  # 将传过来的值去掉前面的0x和中间的空值，并转为list
            for i in range(len(_res)):
                if 2 > len(_res[i]):  # 如果list中的数只有1位则在前面添加0，如5变为05
                    _res[i] = '0' + _res[i]
            res = ''.join(_res)  # 将其转回string
            tg_rcv_unit = res[6:22]  # 取转换之后code的6-22位为tg_rcv_unit
            tg_rcv_code_ox = res[22:25]  # 取转换之后code的22-25位为tg_rcv_code_ox
            tg_code_ox = res[25:30]  # 取转换之后code的25-30位为tg_code_ox

        # 转换之前对不够长度的部分采用了前面补0的方式补长度，所以现在取非0开始的一段数字
        pattern = re.compile(r'[^0][\d\w]*')
        try:
            tg_rcv_unit = pattern.search(tg_rcv_unit).group(0)
            tg_rcv_code_ox = pattern.search(tg_rcv_code_ox).group(0)
            tg_code_ox = pattern.search(tg_code_ox).group(0)
        except Exception as e:
            print(e)
            print(tg_rcv_unit, tg_rcv_code_ox, tg_code_ox)
            tg_rcv_unit = '0000000000000000'
            tg_rcv_code_ox = '000'
            tg_code_ox = '00000'

        # 将tg_code_ox和tg_rcv_code_ox从16进制转回10进制
        try:
            tg_code_ox = int(tg_code_ox, 16)
            tg_rcv_code_ox = int(tg_rcv_code_ox, 16)
        except Exception as e:
            print(e)
            tg_code_ox = ''
            tg_rcv_code_ox = ''

        # 将tg_rcv_unit从unicode_escape编码转回中文，先要在每4个字符前补充\u，因为打印标签时去掉了
        tg_rcv_unit = tg_rcv_unit[len(tg_rcv_unit) - 12:]
        _tg_rcv_unit = []
        for i in range(3):
            _tg_rcv_unit.append(r'\u' + tg_rcv_unit[i * 4:i * 4 + 4])
        try:
            tg_rcv_unit = ''.join(_tg_rcv_unit).encode().decode('unicode_escape')
        except Exception as e:
            print(e)
            _tg_rcv_unit = ''
        tag_info = '【' + tg_rcv_unit + '】' + str(tg_rcv_code_ox)
        try:
            tag_info.encode('utf-8')
        except Exception:
            tag_info = '【】'
        return res[6:30], tag_info, tg_code_ox

    # 发送指令的完整流程
    def send_cmd(self, command):
        # 向串口输入命令
        self.port.write(command)
        # 此处需要循环调用read_all()方法读取串口的返回值
        # 每隔0.05秒读一次，读不到就直接进行下一次读取，不再等待
        # 否则自动等read_all()方法返回需要等上2秒钟时间（这个库本身的原因），十分影响效率
        while True:
            time.sleep(0.15)
            response = self.port.read_all()  # 尝试读取串口的值
            # response = self.port.read_line()
            if response == '':  # 如果值为空，进行下一次读取
                continue
            else:  # 直到有值，跳出循环
                break
        response = self.convert_hex(response)  # 将结果转码
        return response

    # 综合之前的方法，读取tag的值
    def read_tagdata(self):
        cmd_set_antenna = 'A004017400E7'
        cmd_real_time_inventory = 'A004018901D1'
        res = self.send_cmd(bytes.fromhex(cmd_set_antenna))
        if len(res) < 5:
            return 2, ''
        if 16 == int(res[4], 16):
            res = self.send_cmd(bytes.fromhex(cmd_real_time_inventory))
        else:
            return 2, ''
        res = ''.join(res)
        # 结束的返回结果为0xa00xa0x10x89，根据它分割，前面是有用的返回结果
        # 可以用读卡器demo看一下
        res = list(filter(None, res.split('0xa00xa0x10x89')))[:-1]
        res = list(filter(None, ''.join(res).split('0xa00x130x10x89')))
        if 0 >= len(res):
            return 1, ''
        return 0,res


if __name__ == '__main__':
       # print(UHFSocket.parse_code('0000676D5BC653D107A004FF', True))
    cf = configparser.ConfigParser()
    cf.read("uhf_socket.conf")
    url = cf.get("url","target")
    # print(url)
    # sys.exit()

    ser = UHFSocket('COM3')  
    res = ser.read_tagdata()
    if res[0] == 1:
        data = {'result':'1','data':''}
    elif res[0] == 2:
        data = {'result':'2','data':''}   
    elif res[0] == 0:
        string = ser.parse_code("".join(res[1]))
        # print(string[0])
        data = {'result':'0','data':string[0][-8:]}
    print(data)
    r = requests.get(url+'/ComMes.php',params=data)
    print(r.status_code)
    print(r.text)
    if (r.status_code==200 and r.text=='0' and data['data']!=''):
        print("更新成功")
    elif(r.status_code==200 and r.text=='0' and data['data']==''):
        print("清除成功")    
    elif (r.status_code==200 and r.text=='1'):
        print("数据库连接失败")
    elif(r.status_code==200 and r.text=='2'):
        print("数据表更新失败")
    else:
        print("发送失败")        

    input("Press <enter>")        




