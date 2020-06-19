### Docker
	Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从Apache2.0协议开源。
	Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。
	容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。
	
	Docker的应用场景
		Web 应用的自动化打包和发布。
		自动化测试和持续集成、发布。
		在服务型环境中部署和调整数据库或其他的后台应用。
		从头编译或者扩展现有的OpenShift或Cloud Foundry平台来搭建自己的PaaS环境。
		
	Docker 的优点
		1、简化程序：
		Docker 让开发者可以打包他们的应用以及依赖包到一个可移植的容器中，然后发布到任何流行的 Linux 机器上，便可以实现虚拟化。Docker改变了虚拟化的方式，使开发者可以直接将自己的成果放入Docker中进行管理。方便快捷已经是 Docker的最大优势，过去需要用数天乃至数周的	任务，在Docker容器的处理下，只需要数秒就能完成。

		2、避免选择恐惧症：
		如果你有选择恐惧症，还是资深患者。Docker 帮你	打包你的纠结！比如 Docker 镜像；Docker 镜像中包含了运行环境和配置，所以 Docker 可以简化部署多种应用实例工作。比如 Web 应用、后台应用、数据库应用、大数据应用比如 Hadoop 集群、消息队列等等都可以打包成一个镜像部署。

		3、节省开支：
		一方面，云计算时代到来，使开发者不必为了追求效果而配置高额的硬件，Docker 改变了高性能必然高价格的思维定势。Docker 与云的结合，让云空间得到更充分的利用。不仅解决了硬件管理的问题，也改变了虚拟化的方式。
				
		
### Docker镜像常用命令
	docker image pull 下载镜像的命令。镜像从远程镜像仓库服务的仓库中下载。
	docker image ls列出了本地 Docker 主机上存储的镜像	
	docker image inspect命令非常有用！该命令完美展示了镜像的细节，包括镜像层数据和元数据。	
	docker image rm用于删除镜像。	
		
### Docker容器常用命令
	docker container run  启动新容器的命令。该命令的最简形式接收镜像和命令作为参数。镜像用于创建容器，而命令则是希望容器运行的应用。
	docker container ls   列出所有up（在运行）状态的容器	如果使用 -a 标记，还可以看到处于停止（Exited）状态的容器
	docker container exec	用于在运行状态的容器中，启动一个新进程
	docker container stop 	此命令会停止运行中的容器，并将状态置为 Exited(0)。
	docker container start	重启处于停止（Exited）状态的容器。可以在 docker container start 命令中指定容器的名称或者 ID。
	docker container rm		删除停止运行的容器。可以通过容器名称或者 ID 来指定要删除的容器。推荐首先使用 docker container stop 命令停止容器，然后使用 docker container rm 来完成删除。 
	docker container inspect	显示容器的配置细节和运行时信息。该命令接收容器名称和容器 ID 作为主要参数。	
	
	
	
	
#### 步骤
	第一步：安装docker
		Docker命令工具需要root权限才能工作，可以将用户放入组来避免每次都要使用sudo
	第二步：从公共registry下载一个镜像
		docker pull ubuntu:latest
	第三步：列出镜像
|		docker images
	第四步：从该镜像上创建一个容器
		docker run --rm -ti ubuntu /bin/bash
		
		--rm ： 告诉Docker一旦运行的进程退出就删除容器。测试时非常有用 免除杂乱
		-ti : 	告诉Docker分配一个伪终端并进入交互模式
		ubuntu: 这是容器立足的镜像
		/bin/bash： 要运行的命令
	运行一个容器
		docker run -d ubuntu ping 8.8.8.8
		检查容器是否开始运行
		docker ps
		容器被自动分配了一个名称。观察容器里发生了什么
			docker exec -ti test_name /bin/bash
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
		
		