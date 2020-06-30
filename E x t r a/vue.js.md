### vue.js

#### 简介
     是一套用于构建用户界面的渐进式框架。
     Vue 被设计为可以自底向上逐层应用
     引入
     <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
     <script src="https://cdn.jsdelivr.net/npm/vue"></script>
     

#### 基础用法

		1、el:'#app'
			代表id为 app的元素
		2、data 所有的数据都在data中
		3、mes 任何字符串所对应值 
			在html中 {{ mes }} 表示
		4、	修改某个值 响应式 会直接在页面上更新
			var app = new Vue([
				el:'#app',
				data:{
					message:'hello'
				},
			])
			app.message = 'i love you';
			
			<div id="app">{{ message }}</div>
		
		5、绑定元素属性
			v-bind:title="message";                鼠标悬停的提示
			message:'页面记载于'+ new Date().toLocaleString()
		
		6、元素是否显示
			v-if='seen'
			data:{
				seen:true|false
			}
			
		7、循环数组
			<div v-for='val in vals'>{{ val.id }}</div>
			data{
				vals[
				{id:'123'},
				{id:'2345'},
				{id:'4567'}
				]
			}
			app.vals.push({id:'new'})  可以向数组中添加元素
			
		8、点击事件
			<button v-on:click="mes">Message</button>
			methods:{
				Message:function(){
					this.message = this.message.split('').reverse().join('')
				}
			}
			逆转消息
		
		9、同步输入
			{{ message }}
			<input v-model="message">
		
		10、components
			Vue.component('todo-item',{
				props:['todo'],
				template:'<li>{{ todo.text }}</li>'
			})
			var app = new Vue({
				el:"#app",
				data:{
					groceryList:[
					{id:0,text:'Vegetables'},
					{id:1,text:'111'},
					{id:2,text:'222'}
					]
				}
			})
			<div id="app">
				<ol>
					<todo-item>
					</todo-item>
				</ol>
			</div>
			
### 常用
		v-text='mes'
		表示在此元素下的内容 由vue 的 mes值来决定、
		v-html
		不会对标签进行转义
		
		v-on:click="handleClick"
		函数定义在 vue 的methods方法中
		@ 代替 v-on: =>   @click
		
		v-bind:title 	鼠标悬停的提示
		:代替 v-bind: => :title
		
		v-model   双向绑定  模板指定
			
		计算属性
			computed:{
				fullName:function(){
					return this.firstName+''+this.lastName
				}
			}
		侦听器
			data:{
				count:0
			}
			watch:{
				firstName:function(){
					this.count++;
				},
				lastName:function(){
					this.count++;
				},
			}
			
		v-if false时会直接将元素在dom中移除
		v-show false时 会增加 display:none
			
		**组件通信
		<todo-item	v-for="(item,index) of list"
		:key="index"
		:content="item"
		:index="index"
		@delete="handleDelete"
		> </todo-item>
		Vue.component({
		props:['content','index'],
		template:'<li @click="click">{{content}}</li>',
		methods:{
			click.function(){
				this.$emit('delete',this.index);			this.index为参数
			}
		}
		})
		=>在父组件中 创建 handleDelete方法 即可完成通信
			
			
			
			
			
			
			
			
			
			