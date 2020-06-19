<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class comments extends Model
{
    //
    protected $private_key = "id";
    protected $table = "comments";
    public $timestamps = false;
}
