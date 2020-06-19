#### laravel 邮件
		app\config\mail.php 文件中进行配置
			from.address 全局配置邮箱地址
				.name   全局名称
				
			.env 文件配置	
			MAIL_DRIVER=smtp
			MAIL_HOST			服务地址
			MAIL_PORT=465
			MAIL_USERNAME		账号
			MAIL_PASSWORD		密码
			MAIL_ENCRYPTION=SSL	协议 ssl
		
		1、
		Mail:raw('邮件内容',function($message){
			$message->from('wdz@116.com','ifi');
			$message->subject('邮件主题');
			$message->to('261265@qq.com');
		});	
		2、
		Mail::send('student.mail',['name'=>'sean'],function($message){
			$message->to('12323@qq.com');
		});