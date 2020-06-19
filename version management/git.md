git  
====
	--摘自廖雪峰的官方网站

		一、安装

		1、linux
				sudo apt-get install git            //安装git
				sudo adduser git                    //创建git 用来运行git服务
				创建证书登录 id_rsa.pub文件
				sudo git init --bare sample.git     //初始化 Git 仓库
				sudo chown -R git:git sample.git    //将owner 改为git
				git:x:1001:1001:,,,:/home/git:/bin/bash 改为
				git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell       //禁用shell登录
				git clone git@server:/srv/sample.git                   //克隆远程仓库
		2、windows
				下载安装程序
				使用GIT->GIT BASH
			
		完成后进行设置

				git config --global user.name 'myname'
				git config --global user.email 'myemail@example.com'
			
			
		二、创建版本库	
			mkdir my_repository
			cd my_repository 
			git init              //把这个目录变成Git可以管理的仓库
			
			1)基本步骤
				git add test.txt      //把文件添加到仓库
				git commit -m "something about"    //把文件提交到仓库
				
				修改
				git status   //可以让我们掌握仓库的当前状态
				当文件被修改或者有新文件时，将会有提示
				
				git diff     //将会显示当前的文件信息和之前的不同之处  
				此时使用git status会显示modified
				提交add  commit 再使用 git status 仓库状态会=》working tree clean
				
			
			2)版本回退
				每当文件修改到一定程度的时候，就可以 保存一个快照 这个快照在git中被称为commit
				当文件错乱或者误删，可以从最近的一个commit恢复，然后继续工作
				
				git log     	//命令查看版本历史记录
				--pretty=oneline	//参数  输出信息美观 
				
				比如说上个版本名字为 laravel
				可以使用 git reset 命令
				
				git reset --hard HEAD^       //回到上一个版本  HEAD^^ 回到前两个版本
				git reset --hard 2a874       //2a874为之前回退的版本号，找到这个版本号，即可还原
				如果找不到被覆盖的版本号  可以使用命令
				git reflog  记录你的每一次版本号 更替
				
				
			3)管理修改
				git add 放入暂存区 准备提交
				当文件被修改时， git commit 负责把暂存区的修改提交，后面的修改不会被提交
				git diff HEAD -- git.txt 来查看工作区和版本库里面最新版本的区别
				
				
			4)撤销修改
				git checkout --file  可以丢弃工作区的修改
				1 修改后没有被放到暂存区，撤销修改就回到和版本库一模一样的状态
				2 已经添加到暂存区，又做了修改，撤销修改就回到添加到暂存区后的状态
				=》让这个文件回到最近一次 git commit 或 git add时的状态
			
				当文件被 add 但是没有 commit
				git reset HEAD <file> 可以吧暂存区的修改撤销掉，重新放回工作区
				
			
			5)删除文件
				当文件被删除
				1、 从版本库中删除该文件  git rm  git commit
				2、 删错了，恢复误删文件到最新版本
					git checkout -- git.txt
					
					

		三、 远程仓库
				1、添加
				关联一个远程库，使用命令
					git remote add origin git@server-name:path/repo-name.git
				关联后，使用
					git push -u origin master 第一次推送master分支的所有内容
				此后，每次本地提交后，可以使用
					git push origin master 推送最新修改
				
				2、从远程库克隆
					git clone git@github.com:wdzhjj/laravel.git
			

		**********************

		四、分支管理
				
			1) 创建与合并分支
				git 一条时间线里的分支叫做主分支  即 master 分支
				HEAD 不是指向提交，而是指向 master 
				
				当创建一个新的分支，git 新建了一个指针，指向master相同的提交
				再把HEAD 指向dev,表示当前分支在dev上
				再次修改和提交，就是针对dev的分支，dev指针向前移动，master指针不变
				
				假若dev上工作完成了，就可以把dev合并到master上
				=》直接把master指向当前的提交
				
				
				git checkout -b dev      //创建一个新的分支， -b表示创建并切换
				git branch dev           //查看当前分支
				git checkout master      //移动到master分支
				
				=>git merge dev          //合并dev分支的工作内容到master分支上
				
				之后可以删除dev分支
				git branch -d dev
				
				===>鼓励使用分支完成某个任务，合并后再删掉分支，过程更加安全
				
				
			2) 	解决冲突
				当master分支和创建的分支 并非添加关系时
				git merge dev 无法执行合并，只能试图把各自的修改合并起来
				=》冲突 必须手动修改后在提交
				
			
			3)  分支管理策略
				合并分支，git会使用 Fast forward模式。
				这种模式下，删掉分支，会丢失掉分支信息
				如果要强制禁用Fast forward模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。
				git	merge --no-ff -m "merge with no-ff" dev
				
				分支策略
				master分支应该是稳定的，仅用来发布新版本，不在上面干活
				dev分支上工作。与团队都在dev分支上工作，每个人 有自己的分支
				
				--no-ff 参数 可以用普通木事合并，合并后的历史有分支
				而fast forward 看不出曾经有过合并
				
			4)  BUG分支
				每个bug都可以通过一个新的临时分支来修复，修复后，合并分支，然后将临时分支删除。
				stash功能 把当前的工作现场 储藏 起来 等以后恢复现场后继续工作
				git stash
				=>切换到master 解决 bug  
				=>解决后 合并分支
				=>切换到 dev  git checkout dev 
				=>git stash list 查看工作现场
				=>1、 git stash apply 恢复。恢复后 stash内容不删除，需要git stash drop来删除
				=>2、 git stash pop 恢复的同时把stash内容也删了
				
			
			5)  Feature分支
				开发一个新的feature，最好新建一个分支
				如果要丢弃一个没有被合并过的分支
				通过    git branch -D <file>  强行删除
				
			
			6)  多人协作
				查看远程库信息：
					git remote        (-v  查看更详细信息)
				推送分支
					推送时，要指定本地分支，这样，Git就会把该分支推送到远程库对应的远程分支上
					git push origin dev
				抓取分支
					多人写作时，会往各自的master，dev分支上推送各自的修改
					同伴clone仓库
					创建 dev分支 并提交
					=》 使用 git pull 把最新的提交抓下来 在本地 合并
					=》 失败 本地dev分支 与远程分支没有指定链接
					=》 设置dev 和远程 origin/dev的链接   git branch --set-upstream-to=origin/dev dev
					=》 再pull  手动解决并提交
					
				*******
				查看远程库信息       git remote -v
				本地新建的分支 不推送到远程，对其他人不可见
				本地推送分支   git push origin branch-name 如果推送失败 先用 git pull抓取远程的新提交
				在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；
				建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；
				从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。
				
				
			7)  rebase
				rebase 操作可以吧本地未 push的分叉提交历史整理成直线
				rebase 的目的是让我们在查看历史提交的变化时更容易。
				
				
				
		*******************

			五、标签管理
				发布一个版本时，通常在版本库中打一个标签(tag),这样就唯一确定了打标签时刻的版本
				无论何时，取某个标签的版本，就是把那个打标签的时刻的历史版本取出来
				所以标签也是版本库的一个快照，实际上是某个commit的指针，只不过不可以移动
				git branch 查看分支
				git checkout master 切换分支
				git tag v1.0 打新标签
				git tag  查看所有标签
				git tag -a <tagname> -m "sfdsfs" 可以指定标签信息
				git tag -d v1.0      删除标签
				git push origin <tagname>     推送某个标签到远程
				git push origin --tags        一次性推送所有尚未推送的标签
				
				如果标签已经推送到远程，要删除远程标签
					先本地删除
						git tag -d v1.0
					从远程删除
						git push orgigin :refs/tags/v1.0
						
				
			六、自定义git	
				git config --global color.ui true    让git显示颜色
				git config --global alias.st status  设置别名  status => st
				每个仓库的Git配置文件都放在.git/config 文件中
				
				
				
	#### 常用Git命令清单
		日常6个命令
			--------------------------------------------->pull
				--->fetch|clone				----checkout		
		Remote					Repository						Workspace
				--------->push			<--commit	 Index  	add<--
				
				
		Workspace 		工作区		
		Index | Stage	暂存区
		Repository		仓库区|本地仓库
		Remote			远程仓库
		
		1、新建代码库
			# 在当前目录新建一个Git代码库
			$ git init

			# 新建一个目录，将其初始化为Git代码库
			$ git init [project-name]

			# 下载一个项目和它的整个代码历史
			$ git clone [url]
			
		2、配置	
			Git的设置文件为.gitconfig，它可以在用户主目录下（全局配置），也可以在项目目录下（项目配置）。
			# 显示当前的Git配置
			$ git config --list

			# 编辑Git配置文件
			$ git config -e [--global]

			# 设置提交代码时的用户信息
			$ git config [--global] user.name "[name]"
			$ git config [--global] user.email "[email address]"
						
		3、增加删除文件
			# 添加指定文件到暂存区
			$ git add [file1] [file2] ...

			# 添加指定目录到暂存区，包括子目录
			$ git add [dir]

			# 添加当前目录的所有文件到暂存区
			$ git add .

			# 添加每个变化前，都会要求确认
			# 对于同一个文件的多处变化，可以实现分次提交
			$ git add -p

			# 删除工作区文件，并且将这次删除放入暂存区
			$ git rm [file1] [file2] ...

			# 停止追踪指定文件，但该文件会保留在工作区
			$ git rm --cached [file]

			# 改名文件，并且将这个改名放入暂存区
			$ git mv [file-original] [file-renamed]
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
				
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	