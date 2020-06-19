<?php
//传相应的IP和端口创建socket操作
function WebSocket($address,$port){
	$server = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);  //2 1 6
	socket_set_option($server, SOL_SOCKET, SO_REUSEADDR, 1);  // 1接受所有数据包
	socket_bind($server, $address, $port);
	socket_listen($server);
	return $server;
}


//循环挂起websocket通道，进行数据接收，处理，发送
function run(){
	while(true){
		$changes = $this->sockets;
		$write = NULL;
		$except = NULL;
	
	 /*
        //这个函数是同时接受多个连接的关键，我的理解它是为了阻塞程序继续往下执行。
        socket_select ($sockets, $write = NULL, $except = NULL, NULL);
 
        $sockets可以理解为一个数组，这个数组中存放的是文件描述符。当它有变化（就是有新消息到或者有客户端连接/断开）时，socket_select函数才会返回，继续往下执行。
        $write是监听是否有客户端写数据，传入NULL是不关心是否有写变化。
        $except是$sockets里面要被排除的元素，传入NULL是”监听”全部。
        最后一个参数是超时时间
        如果为0：则立即结束
        如果为n>1: 则最多在n秒后结束，如遇某一个连接有新动态，则提前返回
        如果为null：如遇某一个连接有新动态，则返回
        */
		
		socket_select($changes,$write,$except,NULL);
		
		foreach($changes as $sock){
			//如果有新的client 连接进来，则
			if($sock == $this->master){
				//接受一个socket连接
				$client = socket_accept($this->master);
				
				//给新连接进来的socket一个唯一ID
				$key = uniqid();
				$this->sockets[] = $client;		//新接连进来的socket存进连接池
				$this->users[$key] = array(
					'socket'=>$client,			//记录新连接进来的client的socket
					'shou'=>false				//标志该socket资源没有完成握手
				);
			}else
			{
				$len = 0;
				$buffer = '';
				//读取该socket信息，注意：第二个参数是引用传参即接受数据，第三个参数是接收数据的长度
				do
				{
					$l = socket_recv($sock, $buf, 1000, 0);
					$len += $l;
					$buffer .= $buf;
				}while($l==1000);
				
				//根据socket在user池里面查找相应的$k，即键 ID
				$k = $this -> search($sock);
				
				//信息长度小于7，该client的socket为断开连接
				if($len<7){
					$this->send2($k);
					continue;
				}
				
				//判断该socket是否已经握手
				if(!$this->users[$k]['shou']){
					$this->woshou($k,$buffer);    //没握手的握手
				}else{
					//client发送信息，对接收到的信息进行uncode处理
					if($buffer==false){
						continue;
					}
					//不为空，进行消息推送操作
					$this->send($k,$buffer);
				}
			}
		}
		
	}	
		
}  //run function
