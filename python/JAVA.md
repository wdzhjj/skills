### JAVA
#### java基础语法
	* 大小写敏感：JAVA是大小写敏感的
	* 类名：对于所有的类来说，类名的首字母应该大写。如果类名由若干个单词组成，
			那么每个单词的首字母应该大写
	* 方法名：所有的方法名都应该以小写字母开头。如果方法名有若干个单词，
			则后面的每个单词首字母大写
	* 源文件名：源文件名必须和类名相同。		
				当保存文件的时候，你应该使用类名作为文件名保存
				文件名的后缀为.java
	* 主方法入口：所有Java程序由public static void main(String []args)方法开始执行
			
	Java标识符		
		所有的标识符都应该以字母（A-Z或者a-z）,美元符（$）、或者下划线（_）开始
		首字符之后可以是字母（A-Z或者a-z）,美元符（$）、下划线（_）或数字的任何字符组合	
		关键字不能用作标识符
		标识符是大小写敏感的	
			
	Java修饰符		
		访问控制修饰符 : default, public , protected, private	
		非访问控制修饰符 : final, abstract, static, synchronized	
			
	Java变量		
		局部变量	
		类变量（静态变量）	
		成员变量（非静态变量）
	
	Java 关键字		
		访问控制	
					private	私有的
					protected	受保护的
					public	公共的
		类、方法和变量修饰符	
					abstract 	声明抽象
					class	类
					extends	扩充,继承
					final	最终值,不可改变的
					implements	实现（接口）
					interface	接口
					native	本地，原生方法（非Java实现）
					new	新,创建
					static	静态
					strictfp	严格,精准
					synchronized	线程,同步
					transient	短暂
					volatile	易失
		程序控制语句	
					break	跳出循环
					case	定义一个值以供switch选择
					continue	继续
					default	默认
					do	运行
					else	否则
					for	循环
					if	如果
					instanceof	实例
					return	返回
					switch	根据值选择执行
					while	循环
		错误处理	
					assert	断言表达式是否为真
					catch	捕捉异常
					finally	有没有异常都执行
					throw	抛出一个异常对象
					throws	声明一个异常可能被抛出
					try	捕获异常
		包相关	
					import	引入
					package	包
		基本类型		
					boolean	布尔型
					byte	字节型
					char	字符型
					double	双精度浮点
					float	单精度浮点
					int	整型
					long	长整型
					short	短整型
		变量引用	
					super	父类,超类
					this	本类
					void	无返回值
		保留关键字
					goto	是关键字，但不能使用
					const	是关键字，但不能使用
					null	空



#### Java中的类
		public class Dog{
			String breed;
			int age;
			String color;
			void barking(){
			}
			void hungry(){
			}
		}
		局部变量：在方法、狗仔方法或者语句块中定义的变量被称为局部变量
				变量声明和初始化都是在方法中，方法结束后，变量就会自动销毁。
		成员变量：成员变量是定义在类中，方法体之外的变量。
				这种变量在创建对象的时候实例化。成员变量可以被类中方法、构造方法和特定类的语句块访问。
		类变量：类变量也声明在类中，方法体之外，但必须声明为static类型。

		构造方法	
			每个类都有构造方法。如果没有显式地为类定义构造方法，Java编译器将会为该类提供一个默认构造方法。
			在创建一个对象的时候，至少要调用一个构造方法。构造方法的名称必须与类同名，一个类可以有多个构造方法。
		public class Puppy{
			public Puppy(){
			}
		 
			public Puppy(String name){
				// 这个构造器仅有一个参数：name
			}
		}
		
		创建对象
			声明：声明一个对象，包括对象名称和对象类型。
			实例化：使用关键字new来创建一个对象。
			初始化：使用new创建对象时，会调用构造方法初始化对象。
				public class Puppy{
				   public Puppy(String name){
					  //这个构造器仅有一个参数：name
					  System.out.println("小狗的名字是 : " + name ); 
				   }
				   public static void main(String []args){
					  // 下面的语句将创建一个Puppy对象
					  Puppy myPuppy = new Puppy( "tommy" );
				   }
				}

		访问实例变量和方法
			/* 实例化对象 */
			ObjectReference = new Constructor();
			/* 访问类中的变量 */
			ObjectReference.variableName;
			/* 访问类中的方法 */
			ObjectReference.methodName();

		
		源文件声明规则
			一个源文件中只能有一个public类
			一个源文件可以有多个非public类
			源文件的名称应该和public类的类名保持一致
			如果一个类定义在某个包找那个，那么应该放在package语句和类定义之间。如果没有package语句，那么import语句应该在源文件中最前面。
			import语句和package语句对源文件中定义的所有类都有效。在同一源文件中，不能给不同的类不同的包声明。

		Java包
			包主要用来对类和接口进行分类。当开发Java程序时，可能编写成百上千的类，因此很有必要对类和接口进行分类。	

		Import语句
			在Java中，如果给出一个完整的限定名，包括包名、类名，那么Java编译器就可以很容易地定位到源代码或者类。Import语句就是用来提供一个合理的路径，使得编译器可以找到某个类。



#### Java 基本数据类型
		内置数据类型
			byte：
				byte 数据类型是8位、有符号的，以二进制补码表示的整数；
				最小值是 -128（-2^7）；
				最大值是 127（2^7-1）；
				默认值是 0；
				byte 类型用在大型数组中节约空间，主要代替整数，因为 byte 变量占用的空间只有 int 类型的四分之一；
			short：
				short 数据类型是 16 位、有符号的以二进制补码表示的整数
				最小值是 -32768（-2^15）；
				最大值是 32767（2^15 - 1）；
				Short 数据类型也可以像 byte 那样节省空间。一个short变量是int型变量所占空间的二分之一；
				默认值是 0；
			int：
				int 数据类型是32位、有符号的以二进制补码表示的整数；
				最小值是 -2,147,483,648（-2^31）；
				最大值是 2,147,483,647（2^31 - 1）；
				一般地整型变量默认为 int 类型；
				默认值是 0 ；
			long:
				long 数据类型是 64 位、有符号的以二进制补码表示的整数；
				最小值是 -9,223,372,036,854,775,808（-2^63）；
				最大值是 9,223,372,036,854,775,807（2^63 -1）；
				这种类型主要使用在需要比较大整数的系统上；
				默认值是 0L；
			float：
				float 数据类型是单精度、32位、符合IEEE 754标准的浮点数；
				float 在储存大型浮点数组的时候可节省内存空间；
				默认值是 0.0f；
				浮点数不能用来表示精确的值，如货币；
			double：
				double 数据类型是双精度、64 位、符合IEEE 754标准的浮点数；
				浮点数的默认类型为double类型；
				double类型同样不能表示精确的值，如货币；
				默认值是 0.0d；
			boolean：
				boolean数据类型表示一位的信息；
				只有两个取值：true 和 false；
				这种类型只作为一种标志来记录 true/false 情况；
				默认值是 false；
			char：
				char类型是一个单一的 16 位 Unicode 字符；
				最小值是 \u0000（即为0）；
				最大值是 \uffff（即为65,535）；
				char 数据类型可以储存任何字符；

		引用类型
			在Java中，引用类型的变量非常类似于C/C++的指针。引用类型指向一个对象，指向对象的变量是引用变量。这些变量在声明时被指定为一个特定的类型，比如 Employee、Puppy 等。变量一旦声明后，类型就不能被改变了。
			对象、数组都是引用数据类型。
			所有引用类型的默认值都是null。
			一个引用变量可以用来引用任何与之兼容的类型。
			

		*****Java语言支持一些特殊的转义字符序列。
					符号	字符含义
					\n		换行 (0x0a)
					\r		回车 (0x0d)
					\f		换页符(0x0c)
					\b		退格 (0x08)
					\0		空字符 (0x20)
					\s		字符串
					\t		制表符
					\"		双引号
					\'		单引号
					\\		反斜杠
					\ddd	八进制字符 (ddd)
					\uxxxx	16进制Unicode字符 (xxxx)
				
		*****自动类型转换
			整型、实型（常量）、字符型数据可以混合运算
			运算中，不同类型的数据先转化为同一类型，然后进行运算.转换从低级到高级。
				低  ------------------------------------>  高

				byte,short,char—> int —> long—> float —> double 

				1. 不能对boolean类型进行类型转换。
				2. 不能把对象类型转换成不相关类的对象。
				3. 在把容量大的类型转换为容量小的类型时必须使用强制类型转换。
				4. 转换过程中可能导致溢出或损失精度
				5. 浮点数到整数的转换是通过舍弃小数得到，而不是四舍五入，
		
			
#### Java 变量类型		  
		type identifier [ = value][, identifier [= value] ...] ;		
		Java语言支持的变量类型有：
			类变量：独立于方法之外的变量，用 static 修饰。
			实例变量：独立于方法之外的变量，不过没有 static 修饰。
			局部变量：类的方法中的变量。		
				
		Java 局部变量		
			局部变量声明在方法、构造方法或者语句块中；
			局部变量在方法、构造方法、或者语句块被执行的时候创建，当它们执行完成后，变量将会被销毁；
			访问修饰符不能用于局部变量；
			局部变量只在声明它的方法、构造方法或者语句块中可见；
			局部变量是在栈上分配的。
			局部变量没有默认值，所以局部变量被声明后，必须经过初始化，才可以使用。				
				
		JAVA 实例变量		
			实例变量声明在一个类中，但在方法、构造方法和语句块之外；
			当一个对象被实例化之后，每个实例变量的值就跟着确定；
			实例变量在对象创建的时候创建，在对象被销毁的时候销毁；
			实例变量的值应该至少被一个方法、构造方法或者语句块引用，使得外部能够通过这些方式获取实例变量信息；
			实例变量可以声明在使用前或者使用后；
			访问修饰符可以修饰实例变量；
			实例变量对于类中的方法、构造方法或者语句块是可见的。一般情况下应该把实例变量设为私有。通过使用访问修饰符可以使实例变量对子类可见；
			实例变量具有默认值。数值型变量的默认值是0，布尔型变量的默认值是false，引用类型变量的默认值是null。变量的值可以在声明时指定，也可以在构造方法中指定；
			实例变量可以直接通过变量名访问。但在静态方法以及其他类中，就应该使用完全限定名：ObejectReference.VariableName。			
				
				
		JAVA 类变量（静态变量）		
			类变量也称为静态变量，在类中以static关键字声明，但必须在方法构造方法和语句块之外。
			无论一个类创建了多少个对象，类只拥有类变量的一份拷贝。
			静态变量除了被声明为常量外很少使用。常量是指声明为public/private，final和static类型的变量。常量初始化后不可改变。
			静态变量储存在静态存储区。经常被声明为常量，很少单独使用static声明变量。
			静态变量在第一次被访问时创建，在程序结束时销毁。
			与实例变量具有相似的可见性。但为了对类的使用者可见，大多数静态变量声明为public类型。
			默认值和实例变量相似。数值型变量默认值是0，布尔型默认值是false，引用类型默认值是null。变量的值可以在声明的时候指定，也可以在构造方法中指定。此外，静态变量还可以在静态语句块中初始化。
			静态变量可以通过：ClassName.VariableName的方式访问。
			类变量被声明为public static final类型时，类变量名称一般建议使用大写字母。如果静态变量不是public和final类型，其命名方式与实例变量以及局部变量的命名方式一致。	
				
				
				
#### JAVA 修饰符
		** 访问控制修饰符
			default：在同一包内可见，不适用任何修饰符。
					 使用对象：类、接口、变量、方法。
			private：在同一类可见。使用对象：变量、方法
					 不能修饰类（外部类）
			public： 对所有类可见。
					 使用对象：类、接口、变量、方法
			protected：对同一包内的类和所有子类可见。
					   使用对象：变量、方法
					   注意：不能修饰类（外部类）。
		
		** 非访问修饰符
			static 修饰符，用来修饰类方法和类变量。
			final 修饰符，用来修饰类、方法和变量，final修饰的类不能够被继承，
				  修饰的方法不能被继承类重新定义，修饰的变量为常量，是不可修改的。	
			abstract 修饰符，用来创建抽象类和抽象方法。	
			synchronized 和 volatile 修饰符，主要用于线程的编程。	
				synchronized 修饰符
					synchronized关键字声明的方法同一时间只能被一个线程访问。
					synchronized修饰符可以应用于四个访问修饰符。
				transient 修饰符
					序列化的对象包含被 transient 修饰的实例变量时，java 虚拟机(JVM)跳过该特定的变量
					该修饰符包含在定义变量的语句中，用来预处理类和变量的数据类型。	
				
				
#### JAVA 循环结构
		while 循环
			while是最基本的循环，它的结构为：

			while( 布尔表达式 ) {
			  //循环内容
			}
				只要布尔表达式为 true，循环就会一直执行下去。
		do…while 循环
			对于 while 语句而言，如果不满足条件，则不能进入循环。但有时候我们需要即使不满足条件，也至少执行一次。

			do…while 循环和 while 循环相似，不同的是，do…while 循环至少会执行一次。

			do {
				   //代码语句
			}while(布尔表达式);		
							
				注意：布尔表达式在循环体的后面，所以语句块在检测布尔表达式之前已经执行了。 如果布尔表达式的值为 true，则语句块一直执行，直到布尔表达式的值为 false。
				
				
		for循环
			虽然所有循环结构都可以用 while 或者 do...while表示，但 Java 提供了另一种语句 —— for 循环，使一些循环结构变得更加简单。

			for循环执行的次数是在执行前就确定的。语法格式如下：

			for(初始化; 布尔表达式; 更新) {
				//代码语句
			}		
				
				最先执行初始化步骤。可以声明一种类型，但可初始化一个或多个循环控制变量，也可以是空语句。
				然后，检测布尔表达式的值。如果为 true，循环体被执行。如果为false，循环终止，开始执行循环体后面的语句。
				执行一次循环后，更新循环控制变量。
				再次检测布尔表达式。循环执行上面的过程。
				
		Java 增强 for 循环
			Java5 引入了一种主要用于数组的增强型 for 循环。

			Java 增强 for 循环语法格式如下:

			for(声明语句 : 表达式)
			{
			   //代码句子
			}		
				声明语句：声明新的局部变量，该变量的类型必须和数组元素的类型匹配。其作用域限定在循环语句块，其值与此时数组元素的值相等。

				表达式：表达式是要访问的数组名，或者是返回值为数组的方法。
				
				  String [] names ={"James", "Larry", "Tom", "Lacy"};
				  for( String name : names ) {
					 System.out.print( name );
					 System.out.print(",");
				  }
				
		Java switch case 语句		
			switch case 语句语法格式如下：

			switch(expression){
				case value :
				   //语句
				   break; //可选
				case value :
				   //语句
				   break; //可选
				//你可以有任意数量的case语句
				default : //可选
				   //语句
			}
			
		switch case 语句有如下规则：

		switch 语句中的变量类型可以是： byte、short、int 或者 char。从 Java SE 7 开始，switch 支持字符串 String 类型了，同时 case 标签必须为字符串常量或字面量。

		switch 语句可以拥有多个 case 语句。每个 case 后面跟一个要比较的值和冒号。

		case 语句中的值的数据类型必须与变量的数据类型相同，而且只能是常量或者字面常量。

		当变量的值与 case 语句的值相等时，那么 case 语句之后的语句开始执行，直到 break 语句出现才会跳出 switch 语句。

		当遇到 break 语句时，switch 语句终止。程序跳转到 switch 语句后面的语句执行。case 语句不必须要包含 break 语句。如果没有 break 语句出现，程序会继续执行下一条 case 语句，直到出现 break 语句。

		switch 语句可以包含一个 default 分支，该分支一般是 switch 语句的最后一个分支（可以在任何位置，但建议在最后一个）。default 在没有 case 语句的值和变量值相等的时候执行。default 分支不需要 break 语句。


#### JAVA类
		Java Math 类
			Java 的 Math 包含了用于执行基本数学运算的属性和方法，如初等指数、对数、平方根和三角函数。
			Math 的方法都被定义为 static 形式，通过 Math 类可以在主函数中直接调用。

		Number & Math 类方法	
			xxxValue()
				将 Number 对象转换为xxx数据类型的值并返回。
			compareTo()
				将number对象与参数比较。	  大于 1  等于 0 小于 -1
			equals()
				判断number对象是否与参数相等
			valueOf()
				返回一个Number对象指定的内置数据类型
			toString()
				以字符串形式返回值
			parseInt()
				将字符串解析为int类型
			abs()
				返回参数的绝对值
			ceil()
				返回大于等于(>=)给定参数的最小整数
			floor()
				返回小于等于给定参数的最大整数
			rint()
				返回与参数最接近的整数。返回类型为double
			round()
				四舍五入。Math.floor(x+0.5),即将原来的数字加上 0.5 后再向下取整
			min()
				返回两个参数中的最小值
			max()
				返回两个参数中的最大值
			exp()
				返回自然数底数e的参数次方
			log()
				返回参数的自然数底数的对数值
			pow()
				返回第一个参数的第二个参数次方
			sqrt()	
				求参数的算术平方根
			sin()
				求指定double类型参数的正弦值
			asin()
				反正弦值
			toDegrees()
				将参数转换为角度
			toRadians()
				将角度转换为弧度
			random()
				返回一个随机数
				
				
		Character 方法		
			isLetter()
				是否是一个字母
			isDigit()
				是否是一个数字字符
			isWhitespace()
				是否是一个空白字符
			isUpperCase()
				是否是大写字母
			isLowerCase()
				是否是小写字母
			toUpperCase()
				指定字母的大写形式
			toLowerCase()
				指定字母的小写形式
			toString()
				返回字符的字符串形式，字符串的长度仅为1
				
				
		StringBuffer 方法		
		StringBuffer sBuffer = new StringBuffer("地址是：");
			public StringBuffer append(String s)
				将指定字符串追加到此字符序列。
			public StringBuffer reverse()	
				 将此字符序列用其反转形式取代。
			public delete(int start, int end)	
				移除此序列的子字符串中的字符。
			public insert(int offset, int i)	
				将 int 参数的字符串表示形式插入此序列中。
			replace(int start, int end, String str)	
				使用给定 String 中的字符替换此序列的子字符串中的字符。
				
				
				
#### JAVA数组
		声明数组变量
			首先必须声明数组变量，才能在程序中使用数组。下面是声明数组变量的语法：

				dataType[] arrayRefVar;   // 首选的方法
				或
				dataType arrayRefVar[];  // 效果相同，但不是首选方法
				
				如：
					double[] myList;
					double myList[];
					int[] numbers = new int[100];
				
		创建数组
			使用new操作符来创建数组
				arrayReVar = new  dataType[arraySize];
				一、使用 dataType[arraySize] 创建了一个数组。
				二、把新创建的数组的引用赋值给变量 arrayRefVar。
			dataType[] arrayRefVar = new dataType[arraySize];
			另外，你还可以使用如下的方式创建数组。
			dataType[] arrayRefVar = {value0, value1, ..., valuek};	
							
		Arrays 类		
			给数组赋值：通过 fill 方法。
			对数组排序：通过 sort 方法,按升序。
			比较数组：通过 equals 方法比较数组中元素值是否相等。
			查找数组元素：通过 binarySearch 方法能对排序好的数组进行二分查找法操作。	
				
				
#### JAVA日期时间
		java.util 包提供了 Date 类来封装当前的日期和时间。 Date 类提供两个构造函数来实例化 Date 对象。
		第一个构造函数使用当前日期和时间来初始化对象。
		Date( )
		第二个构造函数接收一个参数，该参数是从1970年1月1日起的毫秒数。
		Date(long millisec)
		
		日期比较		
			使用 getTime() 方法获取两个日期（自1970年1月1日经历的毫秒数值），然后比较这两个值。
			使用方法 before()，after() 和 equals()。例如，一个月的12号比18号早，则 new Date(99, 2, 12).before(new Date (99, 2, 18)) 返回true。
			使用 compareTo() 方法，它是由 Comparable 接口定义的，Date 类实现了这个接口。
	
#### Java 休眠(sleep)
		sleep()使当前线程进入停滞状态（阻塞当前线程），让出CPU的使用、目的是不让当前线程独自霸占该进程所获的CPU资源，以留一定时间给其他线程执行的机会。		
			Thread.sleep(1000*3);   // 休眠3秒	
				
				
				
#### Java 构造函数
		如果有一个成员的函数的名字和类的名字完全相同，则在创建这个类的每一个对象的时候都会自动调用这个函数
		=>构造函数
				
		*** 函数重载
			一个类可以有多个构造函数，只要他们的参数表不停
			创建对象的时候给出不同的参数值，就会自动调用不同的构造函数
			通过this()还可以调用其他的构造函数
			一个类里的同名但参数表不同的函数构成了重载关系

#### 子类和子类型
		类定义了子类型
		子类定义了子类型
		子类的对象可以被当做父类的对象来使用
			赋值给父类的变量
			传递给需要父类对象的函数
			放进存放父类对象的容器里
				
#### 抽象函数/抽象类
		抽象函数		表达概念而无法实现具体代码的函数
		抽象类			表达概念而无法构造出实体的类
		
		带有abstract修饰符的函数
		有抽象函数的类一定是抽象类
		抽象类不能制造对象
		可以定义常量
		任何继承了抽象类的非抽象类的对象可以付给这个变量
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
				
				
				
				
				
				
				
				
				
			
			
			
			
			
			
			
			