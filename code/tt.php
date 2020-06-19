<?php
echo '****************client*****************<br/>';
//设置 IP 和 端口
// $port = 1935;
// $ip = '127.0.0.1';
$port = 9998;
// $ip = '111.1.17.225';
$ip = '115.236.18.212';

//超时设计
set_time_limit(0);

//创建TCP协议的socket资源
$socket  = socket_create(AF_INET, SOCK_STREAM, SOL_TCP) or die('socket_create 失败：'.socket_strerror($socket));
echo '创建成功<br/>';
$restult = socket_connect($socket, $ip, $port);
echo '连接成功<br/>';

$in = '创建一个sokcet客服端成功，随机编号='.rand(1000,9999);
if(socket_write($socket, $in, strlen($in))) {
    echo '发送成功，发送信息为'.$in.'<br/>';
} else {
    echo '发送失败，原因为'.socket_strerror($socket).'<br/>';
}

while($out = socket_read($socket, 9998)) {
    echo '接收信息成功，信息为'.$out.'<br/>';
}

echo 'socket关闭<br/>';
socket_close($socket);
echo '关闭完成<br/>';