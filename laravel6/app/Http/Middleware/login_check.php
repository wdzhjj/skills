<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Support\Facades\Session;

class login_check
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        if(!Session::get('login_userid')){
            echo "您还没有登录";
        }
        return $next($request);
    }
}
