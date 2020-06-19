#### blade
		
		定义布局
			@section('sidebar')
			@endsection
			<div>  @yield('content')  </div>
			
			@section    定义了一个内容的片段
			@yield		用于显示给定片段的内容
			
		继承布局
			可以使用Blade提供的 
			@extends
			命令来为子视图指定应该 继承 的布局
			继承Blade视图可使用 @section 命令将内容注入布局的 @section中
			而「主」布局中使用 @yield 的地方会显示这些子视图中的 @section 间的内容
		包含子视图
			@include('shared.errors')
			包含的视图继承父视图中的数据，还可以床底额外参数到被包含的视图
			@include('view.name',['some'=>'data'])
		显示未转义的数据
			默认情况下，Blade 的 {{ }} 语法将会自动调用 PHP htmlspecialchars 函数来避免 XSS 攻击。
			不想数据被转义，你可以使用下面的语法：
				{!! $name !!}
		渲染json
			可以使用 Blade 指令 @json 来代替手动调用 json_encode：
			<script>
				var app = @json($array)
			</script>
		注释
			{{--  xyz  --}}
		
		服务注入
			@inject指令可以用于从服务容器中获取服务，
			传递给@inject的第一个参数是   服务将要被放置到的变量名
			第二个参数是  要解析的服务类名或接口名
			
#### 流程控制
##### if
	@if (count($records) === 1)
    我有一条记录！
	@elseif (count($records) > 1)
		我有多条记录！
	@else
		我没有任何记录！
	@endif
	
		@unless(Auth::check())
			你尚未登录
		@endunless	
	
	@isset($records)
    // $records 被定义并且不为空...
	@endisset

		@empty($records)
			// $records 是「空」的...
		@endempty
	
	身份验证快捷
	@auth
    // 用户已经通过身份认证...
	@endauth

	@guest
		// 用户没有通过身份认证...
	@endguest
	
	Switch
	@switch($i)
    @case(1)
        First case...
        @break

    @case(2)
        Second case...
        @break

    @default
        Default case...
	@endswitch

##### 循环
	@for ($i = 0; $i < 10; $i++)
    目前的值为 {{ $i }}
	@endfor

	@foreach ($users as $user)
		<p>此用户为 {{ $user->id }}</p>
	@endforeach

	@forelse ($users as $user)
		<li>{{ $user->name }}</li>
	@empty
		<p>没有用户</p>
	@endforelse

	@while (true)
		<p>死循环了。</p>
	@endwhile
			
	@foreach ($users as $user)
    @if ($user->type == 1)
        @continue
    @endif

    <li>{{ $user->name }}</li>

    @if ($user->number == 5)
        @break
    @endif
	@endforeach		
	
	循环变量：
	循环时，可以在循环内使用 $loop 变量。
	$loop->first; $loop->last
	$loop->parent->first		通过parent属性获取父循环中的$loop变量
	$loop->index     当前循环迭代的索引
	$loop->ineration	当前循环迭代（从1开始）
	$loop->remaining	循环中剩余迭代数量
	$loop->count;
	$loop->depth		当前循环的嵌套级别
	
	
##### 堆栈	
	Blade 可以被推送到在其他视图或布局中的其他位置渲染的命名堆栈。
	@push('scripts')
		<script src="/example.js"></script>
	@endpush
	你可以根据需要多次压入堆栈，通过 @stack 命令中传递堆栈的名称来渲染完整的堆栈内容：
	<head>
    <!-- Head Contents -->
		@stack('scripts')
	</head>
	
	
##### 自定义if语句
	可以在 AppServiceProvider 的 boot方法中：
	Blade::if('自定义的标签', function($environment){
		return app->environment($environment);
	});
	
	
	
	
	
	
			
			