<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use App\blog;
use App\comments;
use App\User_info;

class Orm extends Controller
{
    //
    public function index(Request $request){
    	$data = DB::table("blog")->get();

    	//一对一   一个blog数据对应一个 user_info数据  $res->author获取user_infoz这条数据的对象
    	// $res = blog::find(1);
    	// $tt = $res->author;
    	// dd($tt);            
    	// $res = blog::find(1);
    	// $tt = $res->comments;
    	// foreach($tt as $v){
    	// 	if($v->parent_id != 0 ){
    	// 		$reply = $v->comment;
    	// 	}
    	// }
    	// dd($reply);

    	$blog = blog::all();
    	$bool = $blog->contains(blog::find(1));     //contains 是否包含指定的模型实例
    	$bool = $blog->diff(blog::whereIn('id',[1,11,14])->get());   //返回不在给定集合中的所有模型
        //except([1,11,14])  返回给定主键外的所有模型
    	dd($bool);
    	return view("orm")->with('data',$data);
    }
}

