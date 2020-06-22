<?php

/**
 * 下载图片
 * Class Spider
 */
class Spider
{

    private $code; // 状态码
    private $message; // 消息
    /**
     * 图片位置的根路径
     * @var string
     */
    private $base_path;

    /**
     * url 对应的路径
     * @var string
     */
    private $url_path;


    /**
     * @param $url
     * @param string $path
     * @return string
     * @throws Exception
     */
    public function downloadImage($url, $path = '1/')
    {
        $this->base_path = $path; // 将传递的路径，主动拼接上根图片目录
        $this->url_path = '/pictures/' . $path;
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_ENCODING, 'gzip');
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);

        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE); // 对认证证书来源的检查
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE); // 从证书中检查SSL加密算法是否存在

        $file = curl_exec($ch);
        curl_close($ch);
        if ($file == false) {
            //  图片下载失败
            $this->code = -1;
            $this->message = '图片下载失败';
            return false;
        }
        //  文件夹时需要添加 / 的
        if (substr($this->base_path, -1, 1) !== '/') {
            $this->base_path = $this->base_path . '/';
        }
        return $this->saveAsImage($url, $file);
    }


    /**
     * 保存图片并返回url
     * @param $url
     * @param $file
     * @return string
     * @throws Exception
     */
    private function saveAsImage($url, $file)
    {
        $extension = pathinfo($url, PATHINFO_EXTENSION); //  获取图片后缀
        $filename = uniqid(microtime(true)) . '.' . $extension; // 为图片生成唯一文件名

        //  如果文件夹不存在，则生成
        if (!file_exists($this->base_path)) {
            $make_path = mkdir($this->base_path, 0777, true);
            if (!$make_path) {
                $this->code = -2;
                $this->message = '保存图片时，创建文件夹';
                return false;
            }
        }

        $resource = fopen($this->base_path . $filename, 'a');
        fwrite($resource, $file);
        fclose($resource);
        return 'http://' . $_SERVER['SERVER_NAME'] . $this->url_path . '/' . $filename;
    }

    /**
     * 获取 message
     * @return string
     */
    public function getMessage()
    {
        return $this->message;
    }

    /**
     * 
     * @return int
     */
    public function getCode()
    {
        return $this->code;
    }
}




