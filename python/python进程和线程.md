#### 进程和线程
		对于操作系统来说，一个任务就是一个进程（Process）
		有些进程还不止同时干一件事，在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。
		由于每个进程至少要干一件事，所以，一个进程至少有一个线程
		
		如果我们要同时执行多个任务怎么办？
		
		多任务的实现有3种方式：
			多进程模式；
			多线程模式；
			多进程+多线程模式。

		
		**多进程模式
			Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
			子进程永远返回0，而父进程返回子进程的ID。	
			一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
			Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
			由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！
			有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

			***multiprocessing
				multiprocessing模块提供了一个Process类来代表一个进程对象，
				multiprocessing模块就是跨平台版本的多进程模块。
			from multiprocessing import Process
			import os
			# 子进程要执行的代码
			def run_proc(name):
				print('Run child process %s (%s)...' % (name, os.getpid()))

			if __name__=='__main__':
				print('Parent process %s.' % os.getpid())
				p = Process(target=run_proc, args=('test',))
				print('Child process will start.')
				p.start()
				p.join()
				print('Child process end.')							
				
			执行结果如下：
			Parent process 928.
			Process will start.
			Run child process test (929)...
			Process end.
	
			创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

			join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。	
				
			**Pool
			如果要启动大量的子进程，可以用进程池的方式批量创建子进程：	
			if __name__=='__main__':
				print('Parent process %s.' % os.getpid())
				p = Pool(4)
				for i in range(5):
					p.apply_async(long_time_task, args=(i,))
				print('Waiting for all subprocesses done...')
				p.close()
				p.join()	
				
				
			*********子进程	
				subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
			import subprocess

			print('$ nslookup www.python.org')
			r = subprocess.call(['nslookup', 'www.python.org'])
			print('Exit code:', r)				
				
				
			进程间通信
			Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。	
							
			

			如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。

			如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

			多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式。

			多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。

			多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。

			在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂。	
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				






















		