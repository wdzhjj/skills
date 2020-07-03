####  RabbitMq 消息队列
	MQ全称为Message Queue，消息队列是系统之间的通信方法；
	RabbitMQ是开源的，实现了AMQP协议的，采用Erlang(面向并发编程语言)编写的，可复用的企业级消息系统；
	
	AMQP（高级消息队列协议）是一个异步消息传递所使用应用层协议规范，为面向消息中间件设计，基于此协议的客户端与消息中间件可以无视消息来源传递消息，
	不受客户端、消息中间件、不同的开发语言环境等条件的限制；
	
	关键词
		Server(Broker):接收客户端连接，实现了AMQP协议的消息队列和路由功能的进程
		Virtual Host: 虚拟主机的概念，类似权限控制组。一个Virtual Host里可以有多个Exchange和Queue。   
		Exchange:交换机，接受生产者发送的消息，并根据Routing Key将消息路由到服务器中的队列Queue。
		ExchangeType: 交换机类型决定了路由消息行为，RabbitMQ中有三种类型Exchange，分别是fanout、direct、topic；
		Message Queue:消息队列，用于存储还未被消费者消费的消息
		Message：由Header和body组成
			Header是由生产者添加的各种属性的集合，包括Message是否被持久化、优先级是多少、由哪个Message Queue接收等；
			body是真正需要发送的数据内容；
		BindingKey：绑定关键字，将一个特定的Exchange和一个特定的Queue绑定起来。	
			
	模式：
		1 点对点的队列
			一个生产者P发送消息到队列Q,一个消费者C接收
		2 工作队列模式Work Queue	
			一个生产者发送消息到队列中，有多个消费者共享一个队列，每个消费者获取的消息是唯一的。
		3 发布/订阅模式Publish/Subscribe	
			一个生产者发送消息，多个消费者获取消息（同样的消息），包括一个生产者，一个交换机，多个队列，多个消费者。
			（1）一个生产者，多个消费者
			（2）每一个消费者都有自己的一个队列
			（3）生产者没有直接发消息到队列中，而是发送到交换机
			（4）每个消费者的队列都绑定到交换机上
			（5）消息通过交换机到达每个消费者的队列
			注意：交换机没有存储消息功能，如果消息发送到没有绑定消费队列的交换机，消息则丢失。
		4 路由模式Routing	
			生产者发送消息到交换机并指定一个路由key，消费者队列绑定到交换机时要制定路由key（key匹配就能接受消息，key不匹配就不能接受消息），
			例如：我们可以把路由key设置为insert ，那么消费者队列key指定包含insert才可以接收消息，消费者队列key定义为update或者delete就不能接收消息。
			很好的控制了更新，插入和删除的操作。
		5 通配符模式Topics	
			此模式实在路由key模式的基础上，使用了通配符来管理消费者接收消息。
			生产者P发送消息到交换机X，type=topic，交换机根据绑定队列的routing key的值进行通配符匹配；
		6.spring集成rabbitmq配置	
			提供了AMQP的一个实现，并且spring-rabbit是RabbitMQ的一个实现，
			
			
			
			