<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class user_info extends Model
{
    protected $primaryKey = 'uid';  //默认id
    protected $table = 'user_info';
    public $timestamps = false;
}
