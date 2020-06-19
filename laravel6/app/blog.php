<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class blog extends Model
{

	//protected $table = ""; //表名
    //protected $primaryKey = '';  //默认id
	//public $incrementing = false;  //指示模型主键是否递增
	//protected $keyType = 'string'  //如果你的主键不是一个整数，你需要将模型上受保护的 $keyType 属性设置为 string：

	//是否自动维护时间戳
	public $timestamps = false;
	//时间戳的格式
	//protected $dateFormat = 'U';

	//数据库连接   Eloquent 模型将使用你的应用程序配置的默认数据库连接。
	// protected $connection = 'connection-name';

	//为某些属性定义默认值
  	// protected $attributes = [
    //      'delayed' => false,
    //  ];

    // 隐藏 JSON 属性
    // protected $hidden = ['password'];






    protected $table = 'blog';

    public function author(){
    	//一对一   对应的表，对应的字段，自己相对应的字段（非id）
    	return $this->hasOne("App\user_info",'uid','user_id');
    }

    public function comments(){
    	return $this->hasMany("App\comments",'content_id','id');
    }

    //user_info 定义  相当于 blog 定义 hasOne
    //comments 定义 belongsToMany 相当于 blog 定义 belongsToMany
    public function cc(){
    	return $this->belongsTo("App\comments",'content_id','id');
    }


}
