### Shell
		Shell简介
		Shell自身是一个用C语言编写的程序，是用户来使用Unix或Linux的桥梁，用户的大部分工作都需要通过Shell来完成。

		可以说：Shell既是一种命令语言，又是一种程序设计语言。
		Shell有两种执行命令的方式：
			* 交互式（Interactive）：解释执行用户的命令，用户输入一条命令，Shell就解释执行一条。
			* 批处理（Batch）：用户事先写一个Shell脚本(Script)，其中有很多条命令，
				让Shell一次把这些命令执行完，而不必一条一条地敲命令。
		在平常应用中，不要用 root 帐号运行 Shell 。作为普通用户，不管您有意还是无意，都无法破坏系统；但如果是 root，那就不同了，只要敲几个字母，就可能导致灾难性后果。
		
#### 常用的Shell类型
		Unix/Linux上常见的Shell脚本解释器有bash、sh、csh、ksh等，习惯上把它们称作一种Shell。
		
		bash	 Bourne Again Shell
			bash是Linux标准默认的shell
			Linux使用它作为默认的shell是因为它有诸如以下的特色：
			*可以使用类似DOS下面的doskey的功能，用方向键查阅和快速输入并修改命令。
			*自动通过查找匹配的方式给出以某字符串开头的命令。
			*包含了自身的帮助功能，你只要在提示符下面键入help就可以得到相关的帮助。
			
		sh
			sh 由Steve Bourne开发，是Bourne Shell的缩写，sh 是Unix 标准默认的shell。
		
		ash
		ash shell 是由Kenneth Almquist编写的，Linux中占用系统资源最少的一个小shell，
					它只包含24个内部命令，因而使用起来很不方便。
					
		csh
			csh 是Linux比较大的内核，它由以William Joy为代表的共计47位作者编成，共有52个内部命令。该shell其实是指向/bin/tcsh这样的一个shell，也就是说，csh其实就是tcsh。				
		ksh
			ksh 是Korn shell的缩写，由Eric Gisin编写，共有42条内部命令。该shell最大的优点是几乎和商业发行版的ksh完全兼容，这样就可以在不用花钱购买商业版本的情况下尝试商业版本的性能了。	
			
			
#### 建立、运行shell	
		新建一个文件，扩展名为sh（sh代表shell），或者其他任意名字，其实扩展名并不影响脚本执行,sh便于分辨
			#！/bin/bash
				echo "hello shell"
				
			#! 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即用哪一个Shell来执行。
			echo 命令用于向窗口输出脚本
		
		运行shell的两种方法
			1、作为可执行程序
				chmod +x ./test.sh	使脚本具有执行权限
				./test.sh 	执行脚本
				注意，一定要写成./test.sh，而不是test.sh。
				运行其它二进制的程序也一样，直接写test.sh，linux系统会去PATH里寻找有没有叫test.sh的，
				而只有/bin, /sbin, /usr/bin，/usr/sbin等在PATH里，你的当前目录通常不在PATH里，所以写成test.sh是会找不到命令的，要用./test.sh告诉系统说，就在当前目录找。
			2、作为解释器参数
				/bin/sh test.sh
				/bin/php test.php
				这种方式运行的脚本，不需要在第一行指定解释器信息，写了也没用。


#### shell 变量
		Shell将其中任何设置都看做文本字符串。
		有两种变量，本地和环境。
		严格地说可以有 4种，但其余两种是只读的，可以认为是特殊变量，它用于向Shell脚本传递参数。
		
		定义变量
			定义变量时，变量名不加美元符号$
				variableName = "value"
		变量名的命名须遵循如下规则：			
			*首个字符必须为字母（a-z，A-Z）。
			*中间不能有空格，可以使用下划线（_）。
			*不能使用标点符号。
			*不能使用bash里的关键字（可用help命令查看保留关键字）。

		使用变量
			使用一个定义过的变量，只要在变量名前面加美元符号（$）即可
				echo $your_name
				echo ${your_name}
				echo "I am good at ${your_name}Script"
		
		只读变量
			使用 readonly 命令可以将变量定义为只读变量，只读变量的值不能被改变。
				myname = "hehe"
				readonly myname
				myname = "123"    //将会报错
		
		删除变量
			unset删除变量
				unset myname
			
		显示所有本地shell变量
			使用set命令显示所有本地定义的Shell变量。

		变量类型
			运行shell时，会同时存在三种变量
			1、局部变量
				局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量
			2、环境变量
				所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
			3、shell特殊变量
				shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行。
		
		********Shell 特殊变量
			$0 , $# , $* , $@ , $? , $$
			
			名称	含义
			$0	    当前脚本的文件名
			$#		传递给脚本或函数的参数个数。
			$*		传递给脚本或函数的所有参数。
			$@		传递给脚本或函数的所有参数。被双引号(" ")包含时，与 $* 稍有不同，下面将会单独讲到。
			$?		上个命令的退出状态，或函数的返回值。
			$$		当前进程的ID。对于 Shell 脚本，就是这些脚本所在的进程ID
			$n		传递给脚本或函数的参数。n 是一个数字，表示第几个参数。例如，第一个参数是$1，第二个参数是$2

		命令行参数
			运行脚本时传递给脚本的参数称为命令行参数。命令行参数用 $n 表示，例如，$1 表示第一个参数，$2 表示第二个参数，依次类推。
			而$0代表当前脚本的文件名。
			$* 和 $@ 的区别
				$* 和 $@ 都表示传递给函数或脚本的所有参数，不被双引号(" ")包含时，都以"$1" "$2" … "$n" 的形式输出所有参数。
				但是当它们被双引号(" ")包含时，"$*" 会将所有的参数作为一个整体，以"$1 $2 … $n"的形式输出所有参数；"$@" 会将各个参数分开，以"$1" "$2" … "$n" 的形式输出所有参数。

		$?获取退出状态
			$? 可以获取上一个命令的退出状态。
			所谓退出状态，就是上一个命令执行后的返回结果。
			退出状态是一个数字，一般情况下，大部分命令执行成功会返回 0，失败返回 1。
			不过，也有一些命令返回其他值，表示不同类型的错误。
			
			
			
#### Shell字符串用法
		Shell中的字符串可以用引号包起来，也可以不用引号。
		用引号的话可以用双引号，也可以用单引号。其单双引号的区别跟PHP相类似。
		加单引号的特点：
			Shell单引号里的任何字符都会被原样输出，单引号字符串中的变量无效；
			Shell单引号字串中不能出现单引号（对单引号使用转义符也不行）。
		加双引号的优点：
			Shell双引号里可以有变量
			Shell双引号里可以出现转义字符
			所以，建议大家在使用Shell时，对字符串要加上引号，而且最好加双引号。
		
		Shell字符串的操作
		${#string}					$string的长度
		${string:position}			在$string中, 从位置$position开始提取子串
		${string:position:length}	在$string中, 从位置$position开始提取长度为$length的子串
		${string#substring}			从变量$string的开头, 删除最短匹配$substring的子串
		${string##substring}		从变量$string的开头, 删除最长匹配$substring的子串
		${string%substring}			从变量$string的结尾, 删除最短匹配$substring的子串
		${string%%substring}		从变量$string的结尾, 删除最长匹配$substring的子串
		${string/substring/replacement}	使用$replacement, 来代替第一个匹配的$substring
		${string//substring/replacement}	使用$replacement, 代替所有匹配的$substring
		${string/#substring/replacement}	如果$string的前缀匹配$substring, 那么就用$replacement来代替匹配到的$substring
		${string/%substring/replacement}	如果$string的后缀匹配$substring, 那么就用$replacement来代替匹配到的$substring
				
		1、输出字符串的长度
			name="wdz"
			echo ${#name}   3
		2、截取字符串
			test='iloveit'
			echo ${test:5}	it
		3、字符串的删除
			test='c:/windows/boot.ini'
			echo ${test#/}		c:/windows/boot.ini
			echo ${test#*/}		windows/boot.ini
			echo ${test##*/}	boot.ini
			echo ${test%/*}		c:/windows
			
			${变量名#substring正则表达式}从字符串开头开始配备substring,删除匹配上的表达式。
			${变量名%substring正则表达式}从字符串结尾开始配备substring,删除匹配上的表达式。
			注意：${test##*/},${test%/*} 分别是得到文件名，或者目录地址最简单方法。
		4、字符串的替换
			test='c:/windows/boot.ini'
			echo ${test/\//\\}       c:\windows/boot.ini
			echo ${test//\//\\}	 c:\windows\boot.ini
			${变量/查找/替换值} 一个“/”表示替换第一个，”//”表示替换所有,当查找中出现了：”/”请加转义符”\/”表示。

			
#### Shell 数组
		在Shell中，用括号来表示数组，数组元素之间用“空格”分割开。
		定义数组的一般形式为：
		array_name=(value1 ... valuen)
		也可以单独定义数组的各个分量
			array_name[0]=value0
			array_name[1]=value1
			可以不使用连续的下标，而且下标的范围没有限制
			
		数组赋值
			直接通过数组名【下标】 就可以对其进行引用赋值,下标不存在则自动添加一个数组元素
			a[1]=100
			echo ${a[*]}
		数组读取
			${array_name[index]}
		数组删除
			unset 数组[下标]，可以清相应的元素，不带下标，清除整个数据
		
		常用操作
			1）shell数组长度
				${#数组名[@或*]} 可以得到数组长度
			2）Shell数组的分片
				直接通过 ${数组名[@或*]:起始位置:长度} 切片原先数组，返回是字符串，中间用“空格”分开，因此如果加上”()”，将得到切片数组。
			3）Shell数组的替换
				数组的替换方法是：${数组名[@或*]/查找字符/替换字符} 该操作不会改变原先数组内容，如果需要修改，可以看上面例子，重新定义数据。


#### shell输出
		echo 命令
			echo是shell的一个内部指令，用于在屏幕上打印出指定的字符串
			echo arg
		转义字符
			Shell使用反斜杠 \ 作为转义字符
		输出变量
			name="linux"
			echo "$linux needs shell"
		输出换行
			echo 命令和其他语言一样，使用 反斜杠+n "\n" 来表示换行
		输出重定向
			Shell可以使用右尖括号（“>”）和两个右尖括号（“>>”）来表示输出的重定向
		保持原样输出
			使用单引号可以保持原样输出，不会对内容进行处理
			echo '$name\"'	   //输出 $name\"

			
#### Shell printf
		Shell printf命令语法
			printf  format-string  [arguments...]
			format-string为描述格式规格的字符串，用来描述输出的排列方式，最好为此字符串加上引号。
			此字符串包含按字面显示的字符以及格式声明，格式声明时特殊的占位符，用来描述如何显示相应的参数
			arguments是与格式声明相对应的参数列表，例如一系列的字符串或变量值。
			格式声明由两部分组成：百分比符号（%）和指示符。
			最常用的格式指示符有两个，%s用于字符串，而%d用于十进制整数。
			格式字符串中，一般字符会按字面显示。转义序列则像echo那样，解释后再输出成相应的字符。格式声明以%符号开头，并以定义的字母集中的一个来结束，用来控制相应参数的输出。
			
		Shell printf命令转义序列	
		\a	警告字符,通常为ASCII的BEL字符
		\b	后退
		\c		不显示输出结果中任何结尾的换行字符，而且任何留在参数里的字符、任何接下来的参数以及任何留在格式字符串中的字符都被忽略。
		\f	换页
		\n	换行
		\r	回车
		\t	水平制表符
		\v	垂直制表符
		\\	反斜杠字符
			
		Shell printf命令格式指示符	
			%c	ASCII字符.显示相对应参数的第一个字符
			%d,%i	十进制整数
			%E	浮点格式([-d].precisionE [+-dd])
			%e	浮点格式([-d].precisione [+-dd])
			%g	%e或%f转换,看哪一个较短,则删除结尾的零
			%G	%E或%f转换,看哪一个较短,则删除结尾的零
			%s	字符串
			%u	不带正负号的十进制值
			%x	不带正负号的十六进制.使用a至f表示10至15
			%%	字面意义的%
			%X	不带正负号的十六进制.使用A至F表示10至15
			
		Shell printf命令精度格式指示符	
			%d,%i,%o,%u,%x,%X	要打印的最小位数.当值的位数少于此数字时,会在前面补零.默认精度为1
			%e,%E	要打印的最小位数.当值的位数少于此数字时,会在小数点后面补零,默认为精度为6.精度为0则表示不显示小数点小数点右边的位数
			%f	小数点右边的位数
			%g,%G	有效位数的最大数目
			%s	
			要打印字符的最大数目
			
		Shell printf命令一些标识符	
			-	将字段里已格式化的值向左对齐
			空格	在正值前置一个空格,在负值前置一个负号
			+	总是在数值之前放置一个正号或负号,即便是正值也是
			#	下列形式选择其一:%o有一个前置的o;
			%x与%X分别前置的0x与0X；
			%e,%E与%f总是在结果中有一个小数点;
			%g与%G为没有结尾的零。
			0	以零填补输出,而非空白.这仅发生在字段宽度大于转换后的情况
			
		字符串向左向右对齐:
		$printf "|%-10s| |%10s|\n" hello world
		输出|hello     | |     world|

		空白标志:
		$printf "|% d| |% d|\n" 15 -15                 
		输出:| 15| |-15|

		+标志:
		$printf "|%+d| |%+d|\n" 15 -15  
		输出:|+15| |-15|

		#标志:
		$printf "%x || %#X\n" 15 15
		输出:f || 0XF

		0标志:
		$printf "%05d\n" 15
		输出:00015	
			
			

#### if else
		if else 有三种格式
			1 if...fi
			2 if...else...fi
			3 if...elif...else...fi
			
		if [ expression ]
		then
			Statements to be executed if expression is true
		fi	
		注意：expression 和方括号([ ])之间必须有空格，否则会有语法错误。	
		
		if ... else 语句也可以写成一行，以命令的方式来运行
			if test $[2*3] -eq $[1+5]; then echo 'The two numbers are equal!'; fi;
		if ... else 语句也经常与 test 命令结合使用	
			if test $[num1] -eq $[num2]
			test 命令用于检查某个条件是否成立，与方括号([ ])类似。

#### for 循环
		for 变量 in 列表
		do	
			command1
			command2
			...
		done
			列表是一组值（数字、字符串等）组成的序列，每个值通过空格分隔。
			每循环一次，就将列表中的值依序放入指定的变量中，然后重复执行命令区域（在do和done 之间），直到所有元素取尽为止。
		for loop in one two tree four
		do
			echo "I am : $loop"
		done

		
#### while 循环
		while command
		do
			Statement(s) to be executed if command is true
		done
			command 为条件测试，如果传回值为0（条件测试为真），则进入循环，执行命令区域，否则不进入循环。
			在执行命令的区域中，应该要有改变条件测试的命令，这样，才有机会在有限步骤后结束执行while循环
			while循环通常用来不断执行一系列命令，也可以用来从输入文件中读取数据；
			命令通常为测试条件。

#### until 循环
		Shell until循环和while循环差不多，区别在于while的条件测试是测真值，until循环则是测假值。
		也就是说，在while循环中，如果条件测试结果为真（传回值为0），就进入循环；在until循环中，如果条件测试结果为真（传回值为0），就跳出循环，如果测试结果为假（传回值不为0），则继续循环。	
			until command
			do
			   Statement(s) to be executed until command is true
			done
			
			
#### 分支语句 case...esac
		case 值 in
		模式1)
			command1
			command2
			command3
			;;
		模式2）
			command1
			command2
			command3
			;;
		*)
			command1
			command2
			command3
			;;
		esac
		
		case后为取值，值后为关键字 in，接下来是匹配的各种模式，每一模式最后必须以右括号结束。
		值可以为变量或常数。
		模式支持正则表达式，可以用以下字符：
			*       任意字串
			?       任意字元
			[abc]   a, b, 或c三字元其中之一
			[a-n]   从a到n的任一字元
			|       多重选择
		匹配发现取值符合某一模式后，其间所有命令开始执行直至 ;;。
		;; 与其他语言中的 break 类似，意思是不执行接下来的语句而是跳到整个 case 语句的最后。
		*)与default相似，如果上面没有匹配到的模式，则执行*)里的内容。				
			
			
#### Select
		select name   [in   list ] 
		do 
			statements that can use  $name... 
		done	
		select首先会产生list列表中的菜单选项，然后执行下方do…done之间的语句。用户选择的菜单项会保存在$name变量中。	
		select命令使用PS3提示符，默认为(#?)；	
		在Select使用中，可以搭配PS3=’string’来设置提示字符串。	
			
			
#### Shell 函数
		因为函数是脚本类语言，在执行时是逐行执行的，因此，Shell 函数必须先定义后使用。
			[ function ] funname [()]
			{
				command;
				[return int;]
			}
		function 关键词是可选项，可加可不加。
		大括号内饰函数体，最后是返回值，可以加【return】关键词来指定函数返回内容，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n（0-255）。
		
		Shell函数参数处理		
			在Shell中，调用函数时可以向其传递参数。	
			在函数体内部，通过 $n 的形式来获取参数的值，例如，$1表示第一个参数，$2表示第二个参数，$0代表脚本本身。
			function fSum()
			{
				echo return $(($1+$2))
			}
			fSum 5 7
			
			
#### Shell输入输出重定向
		linux文件描述符
			Linux的文件描述符可以理解为linux跟踪打开文件，而分配的一个数字，这个数字有点类似c语言操作文件时候的句柄，通过句柄就可以实现文件的读写操作。
			用户可以自定义文件描述符范围是：3-max，max跟用户的ulimit –n 定义数字有关系，不能超过最大值。
			linux启动后，会默认打开3个文件描述符，分别是：
			1）标准输入standard input——0
			2）正确输出standard output——1
			3）错误输出：error output——2
			对于所有运行的Shell命令，都会有默认3个文件描述符。
			在一个Shell命令执行时，会先有一个输入：可以从键盘输入，也可以从文件得到
			在命令执行完成后：成功了，会把成功结果输出到屏幕，正确输出默认是屏幕。
			命令执行有错误：会把错误也输出到屏幕上面，错误输出默认也是指的屏幕。
		
		Shell输出重定向
			command-line1 [1-n] > file或文件操作符或设备
			command-line1 [1-n] >>  file或文件操作符或设备
			当使用“>”时，系统会判断右边文件是否存在，如果存在就先删除，并且创建新文件。不存在则直接创建。因此无论左边命令执行是否成功，右边文件都会变为空。
			当使用“>>”操作符时，系统会判断右边文件是否存在，如果不存在，先创建。然后以添加方式打开文件，系统会分配一个文件描述符与左边的标准输出【1】或错误输出【2】绑定。
		
			命令格式				命令说明
			Command > filename		把标准输出重定向到一个文件中
			Command > filename 2>&1	把标准输出和错误一起重定向到一个文件中
			Command 2 > filename	把标准错误重定向到一个文件中
			Command 2 >> filename	把标准输出重定向到一个文件中（追加）
			Command >> filename2>&1	把标准输出和错误一起重定向到一个文件（追加）
		
		Shell输入重定向
			Shell输入重定向主要用向左的尖括号（小于号）“<”表示，命令格式如下：
				command-line [n] <file或文件描述符&设备
		
		
#### Shell文件包含
		Shell文件包含格式
		Shell文件包含的格式如下，使用点号“.”+文件名包含：
			. filename
		或者source+文件名：
			source filename
		
		
#### 常用运算符	
		一、文件比较运算符 
			1. e filename 如果 filename存在，则为真 如： [ -e /var/log/syslog ] 
			2. -d filename 如果 filename为目录，则为真 如： [ -d /tmp/mydir ] 
			3. -f filename 如果 filename为常规文件，则为真 如： [ -f /usr/bin/grep ] 
			4. -L filename 如果 filename为符号链接，则为真 如： [ -L /usr/bin/grep ] 
			5. -r filename 如果 filename可读，则为真 如： [ -r /var/log/syslog ] 
			6. -w filename 如果 filename可写，则为真 如： [ -w /var/mytmp.txt ] 
			7. -x filename 如果 filename可执行，则为真 如： [ -L /usr/bin/grep ] 
			8. filename1-nt filename2 如果 filename1比 filename2新，则为真 如： [ 
			/tmp/install/etc/services -nt /etc/services ] 
			9. filename1-ot filename2 如果 filename1比 filename2旧，则为真 如： [ 
			/boot/bzImage -ot arch/i386/boot/bzImage ]
		
		二、字符串比较运算符（请注意引号的使用，这是防止空格扰乱代码的好方法） 
			 1. -z string  如果 string长度为零，则为真 如：  [ -z "$myvar" ]
			 2. -n string  如果 string长度非零，则为真  如： [ -n "$myvar" ]
			 3. string1= string2  如果 string1与 string2相同，则为真 如：  ["$myvar" = "one two three"]
			 4. string1!= string2  如果 string1与 string2不同，则为真 如：  ["$myvar" != "one two three"]
		
		
		三、算术比较运算符 
			 1. num1-eq num2  等于 如： [ 3 -eq $mynum ]
			 2. num1-ne num2  不等于 如： [ 3 -ne $mynum ]
			 3. num1-lt num2  小于 如： [ 3 -lt $mynum ]
			 4. num1-le num2  小于或等于  如：[ 3 -le $mynum ]
			 5. num1-gt num2  大于  如：[ 3 -gt $mynum ]
			 6. num1-ge num2  大于或等于 如： [ 3 -ge $mynum ]
		
		四、查看磁盘、文件大小 
			1. df -h 查看磁盘占用情况 
			2、du -sm ./* 查看当前目录下文件大小，单位M
					
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		




			



