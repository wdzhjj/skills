## mysql 

### mysql基础
		SELECT 
			column_1,column_2,...  (列)
		FROM
			table_1
		[INNER | LEFT | RIGHT] JOIN table_2 ON conditions
		WHERE
			conditions
		GROUP BY 
			column_1
		HAVING
			group_conditions
		ORDER BY
			column_1
		LIMIT offset,length
			
			
		SELECT * 使用星号(*)可能会返回不使用的列的数据。 它在MySQL数据库服务器和应用程序之间产生不必要的I/O磁盘和网络流量。
				 如果明确指定列，则结果集更可预测并且更易于管理。
				使用星号(*)可能会将敏感信息暴露给未经授权的用户。
		WHERE 子句中的运算符
				BETWEEN 选择在给定范围内的值
				LIKE 匹配基于模式匹配的值
				IN 指定值是否匹配列表中的任何值
				IS NULL 检查该值是否为 NULL
	
		*插入数据
		INSERT INTO TABLE(column_1,column_2...)
			VALUES (value1,value2,...);
		插入多行
			INSERT INTO TABLE(column_1,column_2...)
			VALUES (value1,value2,...),
				   (value1,value2,...),
	
		*更新数据
			UPDATE [LOW_PRIORITY] [IGNORE] table_name
			SET
				column_1 = expr1,
				column_2 = expr2,
				...
			WHERE
				condition;
				
			LOW_PRIORITY修饰符指示UPDATE语句延迟更新，直到没有从表中读取数据的连接。 
			LOW_PRIORITY对仅使用表级锁定的存储引擎(例如MyISAM，MERGE，MEMORY)生效。	
			即使发生错误，IGNORE修饰符也可以使UPDATE语句继续更新行。导致错误(如重复键冲突)的行不会更新。
		
		*删除数据
			DELETE FROM table_name
			WHERE condition;
			where子句是可选的，省略where，delete将删除表中所有行
	
		**创建删除数据库
			CREATE DATABASE [IF NOT EXISTS] database_name;
				IF NOT EXISTS 可选子句防止创建数据库服务器中已存在的数据库错误
			SHOW DATABASES 语句显示MYSQL数据库服务器中的所有数据库
			USE database_name 使用数据库
			
			DROP DATABASE [IF EXISTS] database_name;
				DROP DATABASE是要删除的数据库名称
				IF EXISTS是该语句的可选部分，以防止您删除数据库服务器中  不存在的数据库。
		**创建表
			CREATE TABLE [IF NOT EXISTS] table_name(
				column_list
			) engine=table_type
			column_list 为表定义列，语法为
			column_name data_type[size] [NOT NULL|NULL][DEFAULT value][AUTO_INCREMENT]
			指定主键
				PRIMARY KEY (col1,col2,...)  加在column_list中
		**修改表结构
			ALTER TABLE table_name action1[,action2,...]
			操作可以是添加新列，添加主键，重命名表等任何操作。ALTER TABLE语句允许在单个ALTER TABLE语句中应用多个操作，每个操作由逗号(，)分隔
			* 设置列的自动递增属性
				CHANGE COLUMN task_id task_id INT(11) NOT NULL AUTO_INCREMENT
			* 增加新列到表中
				ADD COLUMN complete DECIMAL(2,1) NULL
				AFTER description;
			* 从表中删除列
				DROP COLUMN description
			* 重命名表
				RENAME TO work_intems
				
#### 连接查询
		连接查询：将多张表（大于等于 2 张表）按照某个指定的条件进行数据的拼接，其最终结果记录数可能有变化，但字段数一定会增加。
			交叉连接：cross join，从一张表中循环取出每一条记录，每条记录都去另外一张表进行匹配，匹配的结果都保留（没有条件匹配），
				  而连接本身的字段会增加，最终形成的结果为笛卡尔积形式。
				  左表 cross join 右表;
			内连接：inner join，从左表中取出每一条记录，和右表中的所有记录进行匹配，并且仅当某个条件在左表和右表中的值相同时，
				    结果才会保留，否则不保留。	  
				    基本语法：左表 + [inner] + join + 右表 + on + 左表.字段 = 右表.字段;
			外连接
				外连接：left\right join，以某张表为主表，取出里面的所有记录，然后让主表中的每条记录都与另外一张表进行连接，不管能否匹配成功，其最终结果都会保留，匹配成功，则正确保留；匹配失败，则将另外一张表的字段都置为NULL.
				基本语法：左表 + left\right + join + 右表 + on + 左表.字段 = 右表.字段;			
				left join：左外连接（左连接），以左表为主表；
				right join：右外连接（右连接），以右表为主表。
			自然连接：
				nature join，自然连接其实就是自动匹配连接条件，系统以两表中同名字段作为匹配条件，如果两表有多个同名字段，那就都作为匹配条件。在这里，自然连接可以分为自然内连接和自然外连接。	

			
#### MYSQL聚合函数				
		cout()：统计分组后，每组的总记录数；
		max()：统计每组中的最大值；
		min()：统计每组中的最小值；
		avg()：统计每组中的平均值；
		sum()：统计每组中的数据总和。
		select sex,count(*),max(age),min(age),avg(age),sum(age) from student group by sex;
		count()函数里面可以使用两种参数
			1、 * 表示统计组内全部记录的数量
			2、 字段名表示统计对应字段非null记录的总数。 使用group by进行分组之后，展示的记录会根据分组的字段值进行排序，默认为升序

#### MYSQL 视图
		创建基本语法：create view + 视图名 + as + select语句;
		查询视图：desc+视图名
				  show tables+视图名
				  show create table+视图名
		使用视图：在操作数据库表的过程中，使用视图，主要就是为了查询，因此将视图当做表一样查询即可。
				  在这里需要注意的是，虽然我们说视图是一个虚拟表，它不保存数据，但是它却可以获取数据。	
		修改视图：alter view + 视图名 + as +新的select语句		  
		删除视图：drop view + 视图名		
		视图意义
			视图可以节省 SQL 语句，将一条复杂的查询语句用视图来进行封装，以后可以直接对视图进行操作；
			数据安全，视图操作主要是针对查询的，如果对视图结构进行处理，例如删除，并不会影响基表的数据；
			视图往往在大型项目中使用，而且是多系统使用，可以对外提供有用的数据，但是隐藏关键（或无用）的数据；
			视图是对外提供友好型的，不同的视图提供不同的数据，就如专门对外设计的一样；
			视图可以更好（或者说，容易）的进行权限控制。
		新增数据：多表视图不能新增数据
				  可以向单表视图新增数据，但视图中包含的字段必须有基表中所有不能为空的字段。
		删除数据：多表视图不能删除数据
				  单表视图可以删除数据
		更新数据：无论多表视图还是单表，都可以进行数据的更新		  
		
		视图算法：
			系统对视图以及外部查询视图的select语句的一种解析方式			
			undefined：未定义（默认的），这不是一种实际使用的算法，而是一个“推卸责任”的算法。在未定义的情况下，告诉系统，视图没有定义算法，请自己选择。
			temptable：临时表算法，系统先执行视图的select语句，后执行外部查询语句。
			merge：合并算法，系统先将视图对应的select语句与外部查询视图的select语句进行合并，然后再执行。此算法比较高效，且在未定义算法的时候，经常会默认选择此算法。
			基本语法：create + [algorithm = temptable/merge/undefined] + view + 视图名 + as + select语句;

#### 数据备份与还原			
		单表数据备份
			每次只能备份一张表，而且只能备份数据，不能备份表结构。
			select */字段列表 + into outfile + '文件存储路径' + from 数据源;
			前提导出的外部文件不存在，即文件存储路径下的文件不存在。
				如：select * into outfile 'D:/CoderLife/testMySQL/class.txt' from class;
			
			单表数据备份的高级操作			
				基本语法：select */字段列表 + into outfile + '文件存储路径' + fields + 字段处理 + lines + 行处理 + from 数据源;
				字段处理：
					enclosed by：指定字段用什么内容包裹，默认是，空字符串；
					terminated by：指定字段以什么结束，默认是\t，Tab键；
					escaped by：指定特殊符号用什么方式处理，默认是\\，反斜线转义。
				行处理：
					starting by：指定每行以什么开始，默认是，空字符串；
					terminated by：指定每行以什么结束，默认是\r\n，换行符。
			数据恢复
				基本语法：load data infile + '文件存储路径' + into table + 表名 + [字段列表] + fields + 字段处理 + lines + 行处理;
		
		SQL备份
			mysqldump.exe -hPup + 数据库名字 + [表名1 + [表名2]] > 备份文件目录
				h：IP或者localhost;
				P：端口号
				u：用户名
				p：密码
	
#### 事务
		1、开启事务	
			start transaction;
		2、提交事务
			commit;
		3、回滚事务
			rollback;
		回滚点：在某个操作成功完成之后，后续的操作有可能成功也有可能失败，但无论后续操作的结果如何，前一次操作都已经成功了，因此我们可以在当前成功的位置，
				设置一个操作点，其可以供后续操作返回该位置，而不是返回所有操作，这个点称之为回滚点。关于回滚点的基本语法为，
			设置回滚点：savepoint + 回滚点名称;
			返回回滚点：rollback to + 回滚点名称;
		自动事务:
			在 MySQL 中，默认的都是自动事务处理，即用户在操作完成之后，其操作结果会立即被同步到数据库中。
			开启自动事务处理：set autocommit = on / 1;
			关闭自动事务处理：set autocommit = off / 0;
#### 数据库变量
		系统变量
			show variables;
			查看具体变量：
				select + @@变量名 + [,@@变量名1,@@变量名2...];
			修改全局级别变量：
				set global 变量名 = 值；
		对话级别变量：
			仅对当前客户端当次连接有效
			修改：
				基本语法 1：set 变量名 = 值;
				基本语法 2：set @@变量名 = 值;
		
		自定义变量：
			set @变量名 = 值；
			查看自定义变量：
				select @变量名
			
### 触发器
		触发器：trigger，是指事先为某张表绑定一段代码，当表中的某些内容发生改变（增、删、改）的时候，
			    系统会自动触发代码并执行。
		触发器包含三个要素：
			事件类型：增删改。insert、delete、update
			触发时间：事件类型前和后，before和after
			触发对象：表中的每一条记录（行）
			每张表只能拥有一种触发时间的一种事件类型的触发器，即每张表最多可以拥有 6 种触发器。
			
		创建触发器：
			delimiter 自定义符号 -- 临时修改语句结束符，在后续语句中只有遇到自定义符号才会结束语句
			create trigger + 触发器名称 + 触发器时间 + 事件类型 on 表名 for each row
			begin -- 代表触发器内容开始
			-- 触发器内容主体，每行用分号结尾
			end -- 代表触发器内容结束
			自定义符号 -- 用于结束语句
			delimiter ; -- 恢复语句结束符
				例子
					（-- 创建触发器
					delimiter $$ -- 临时修改语句结束符
					create trigger after_order after insert on orders for each row
					begin -- 触发器内容开始
						-- 触发器内容主体，每行用分号结尾
						update goods set inventory = inventory - 1 where id = 1;
					end -- 触发器内容结束
					$$ -- 结束语句
					delimiter ; -- 恢复语句结束符）
		查询触发器：
			show triggers + [like 'pattern'];
			show triggers\G;  \G表示旋转
			show create trigger + 触发器名称； 查询创建触发器的语句
		删除触发器：
			drop trigger + 触发器名称
			
#### 代码执行结构
		* 顺序结构
		* 分支结构
		* 循环结构
		分支结构
			if 条件判断 then
				-- 满足条件时，要执行的代码
			else -- 可以没有 else 语句
				-- 不满足条件时，要执行的代码
			end if;
		循环结构
			while 条件判断 do
					--满足条件时 要执行的代码
					--变更循环条件
			end while	
				
		interate:迭代，类似于 continue，表示结束本次循环，不执行后续步骤，直接开始下一次循环
		leave：离开，类似于break，直接结束整个循环
			interate/leave + 循环名称。
				循环名称: while 条件判断 do
				-- 满足条件时要执行的代码
				-- 变更循环条件
				iterate/leave 循环名称; -- 控制循环语句
				end while;

#### 存储过程
		procedure 一种用来处理数据(增删改)的方式，可以理解为没有返回值的函数
		创建过程
			-- 基本语法
			create procedure 过程名([参数列表])
			begin
				--过程体
			end	
					(create procedure pro()
					select * from student;)
		查看过程
			show create procedure + 过程名
		调用过程
			call + 过程名
		修改\删除过程
			过程只能先删除后新增，不能修改
			drop procedure + 过程名
			
		过程函数		
			in，数据只是从过程外部传入给过程内部使用，可以是数值也可以是变量；
			out，此参数只能传递变量，且变量指向的数据需要先清空然后才能进入过程内部，该引用供过程内部使用，过程结束后可以将变量的值传递给过程外部使用；
			inout，此参数只能传递变量，该变量的值可以给过程内部使用，过程结束后可以变量的值传递给过程外部使用。
			=》procedure 过程名(in 参数名字 参数类型, out 参数名字 参数类型, inout 参数名字 参数类型)
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
### MYSQL 数据类型
#### 整数型
		tinyint:迷你整型，使用1个字节存储数据
		smallint:小整型，使用2个字节存储数据
		mediumint:中整型，使用三个字节存储数据
		int：标准整型，使用4个字节存储数据
		bigint：大整型，使用8个字节
#### 小数型
		带有小数点或者范围超出整型的数值类型
		浮点型
			float：单精度，占用4个字节存储数据，精度范围大约为七位左右
				直接用float，表示没有小数部分，如果用float(M,D)，其中M代表总长度，D代表小数部分长度，M-D则为整数部分长度
			double：双精度，占用8个字节存储数据，精度十五位左右
		定点型
			decimal
			定点型数据，绝对的保证整数部分不会被四舍五入，也就是说不会丢失精度，
			但小数部分有可能丢失精度，虽然理论上小数部分也不会丢失精度。
#### 日期时间型
		datetime:日期时间，格式为yyyy-MM-dd HH:mm:ss
		date:日期，datetime的date部分
		time：时间，或者说是时间段，为指定的某个时间区间之间，包含正负时间；
		timestamp：时间戳，但并不是真正意义上的时间戳，其是从1970年开始计算的，格式和datetime一致；
		year：年份，共有两种格式，分别为year(2)和year(4).
#### 字符串型
		char(L):L length 可以存储的长度，单位为字符，最大长度为 255
		varchar(L):L length 理论长度65536，但是会多出 1 到 2 个字节来确定存储的实际长度；
		varchar(10)：例如存储 10 个汉字，在 UTF8 环境下，需要 10*3+1=31 个字节。
	
		定长字符串对磁盘空间比较浪费，但是效率高：如果数据基本上确定长度都一样，就使用定长字符串，例如身份证、电话号码等；
		变长字符串对磁盘空间比较节省，但是效率低：如果数据不能确定长度（不同的数据有变化），就使用变长字符串，例如地址、姓名等。
#### 文本字符串
		text：存储文字
		blob：存储二进制数据，通常不用（实际上都是存储路径）
#### 枚举字符串
		enum（‘元素1’，‘元素2’...）
		存储的数据，只能是事先定义好的数据
#### 集合字符串
		set  和枚举类似，实际存储的是数值而不是字符串
		定义： set，元素列表
		使用：可以使用元素列表中的多个元素，用逗号分隔
		
#### 增加主键
		SQL操作中，有3种方法可以给表增加主键
		1、在创建表的时候，直接在字段之后，添加primary key关键字
			number char(10) primary key comment '学号'
		2、	在创建表的时候，在所有的字段之后，使用primary key(主键字段列表)来创建主键（如果有多个字段作为主键，则称之为复合主键）
			primary key(number,course)
		3、当表创建完之后，额外追加主键。可以直接追加主键，也可以通过修改表字段的属性追加主键
			alter table my_pri3 add primary key(course);
		更新、删除主键
			对于主键，没有办法直接更新，主键必须先删除，然后才能更新
			alter table + 表名 + drop primary key;
#### 唯一键
		增加唯一键的三种方法
		1、创建表时，字段后面直接添加 unique或者unique key关键字
		2、在所有字段之后，增加unique key(字段列表)，可以设置复合唯一键
		3、在创建表之后，增加唯一键  
			alter table my_unique3 add unique key(number);
		唯一键与主键本质相同，区别在于：唯一键允许字段值为空，并且允许多个空值存在。
		
#### 索引
		索引：系统根据某种算法，将已有的数据（未来可能新增的数据），单独建立一个文件，这个文件能够实现快速匹配数据，
			  并且能够快速的找到对应的记录，几乎所有的索引都是建立在字段之上的。
			MySQL 中提供了多种索引，包括：

				主键索引primary key
				唯一键索引unique key
				全文索引fulltext index
				普通索引index
		索引的意义：
			提升查询数据的效率；
			约束数据的有效性。
		但是增加索引是有前提条件的，这是因为索引本身会产生索引文件（有的时候可能会比数据本身都大），因此非常耗费磁盘空间。
		如果某个字段需要作为查询的条件经常使用，可以使用索引；
		如果某个字段需要进行数据的有效性约束，也可以使用索引（主键或唯一键）。

### 范式
		Normal Farmat是为了解决数据的存储和优化问题	
		1NF
			第一范式：在设计表存储数据的时候，如果表中设计的字段存储的数据，在取出来使用之前还需要额外的处理（拆分），那么表的设计就不满足第一范式，
			第一范式要求字段的数据具有原子性，不可再分。
		2NF
			第二范式：在数据表的设计过程中，如果有复合主键（多字段主键），且表中有字段并不是由整个主键来确定，而是依赖复合主键中的某个字段（主键的部分），
			也就是说存在字段依赖主键的部分的问题（称之为部分依赖），第二范式就是要解决表设计中不允许出现部分依赖。
		3NF
			第三范式：需要满足第一范式和第二范式，理论上讲，每张表中的所有字段都应该直接依赖主键（逻辑主键，代表是业务主键），如果表设计中存在一个字段，
			并不直接依赖主键，而是通过某个非主键字段依赖，最终实现主键依赖（把这种不是直接依赖主键，而是依赖非主键字段的依赖关系，称之为传递依赖），
			第三范式就是要解决表设计中出现传递依赖的问题。
		逆规范化
			在某些特定的环境中（例如淘宝数据库），在设计表的时候，如果一张表中有几个字段是需要从另外的表中去获取数据，理论上讲，
			的确可以获得想要的数据，但是相对来说，其效率低会一点。此时为了提高查询效率，咱们会刻意的在某些表中，不去保存另外一张表的主键（逻辑主键），
			而是直接保存想要存储的数据信息，这样的话，在查询数据的时候，这张表就可以直接提供咱们想要的数据，而不需要多表查询，但是这样做会导致数据冗余。
			实际上，逆规范化是磁盘利用率和效率之间的对抗。
		
### 蠕虫复制
		从已有的数据表中获取数据，然后将数据进行新增操作
		根据已有表创建新表=》复制表结构
			create table + 表名 + like + [数据库名.]表名;
		蠕虫复制的步骤为：先查出数据，然后将查出的数据新增一遍。
		基本语法：insert into + 表名 + [()] + select + 字段列表/* + from + 表名;
			如  insert into my_copy select * from my_collate_bin;
			
		
		
				

	
	
	
	
### MYSQL常用进阶
	
	
#### 查看mysql数据库及编码格式
		1、查看数据库编码格式
			show variables like 'character_set_database';
		2、查看数据表的编码格式
			show create table table_name;
		3、创建数据库时指定数据库的字符集
			create database dbname character set utf8;
		4、创建数据表时指定数据表的编码格式
			create table table_name(
				name varchar(45) not null,
				price double not null
			)default charset = utf8;
		5、修改数据库的编码格式
			alter database dbname character set utf8;
		6、修改数据表格编码格式
			alter table table_name character set utf8;
		7、修改字段编码格式
			alter table <表名> change <字段名> <字段名> <类型> character
		8、添加外键
			alter table 表名 add constraint 外键名 foreign key 字段名 REFERENCES 外表表名 字段名
		9、删除外键
			alter table 表名 drop foreign key 外键名
	

#### mysqldump备份数据库
		只导出表结构 不导出数据
			mysqldump --opt -d dname -uroot -p >xxx.sql
		备份数据库
			mysqldump dname > bakname
			mysqldump -A -uroot -p dname > bakname;
			mysqldump -d -A --add-drop-table -uroot -p >bakname.sql
		导出数据不导出结构
			mysqldump -t dbname -uroot -p > xxx.sql
		导出数据和表结构
			mysqldump 数据库名 -uroot -p >xxx.sql
		导出特定表结构
			mysqldump -uroot -p -B 数据库名 --table 表名 > xxx.sql
			
#### mysql查看当前数据库
		1、select database();
		2、show tables;   =>会显示 table_in_ ...
		3、status         =>current database
		
#### Truncate
		Truncate Table 用来删除表中的所有行,而不记录单个行操作。
		TRUNCATE TABLE 比DELETE速度更快，使用的系统资源和事务日志资源更少
		当不需要该表时，用drop；保留表，删除所有记录，使用truncate；当你要删除部分记录时,用 delete.
		不可对以下表使用TRUNCATE
			1、用FOREIGN KEY 约束引用的表
			2、参与索引视图的表
			3、通过使用事务复制或合并复制发布的表
			4、TRUNCATE TABLE 不能激活触发器，因为该操作不记录各个行删除
					

					
					
### Mysql 权限	
		grant all privileges on *.* to jack@'localhost' identified by 'jack' with grant option
		grant命令
			all privileges 表示所有权限，也可用select、update
			on 指定权限针对哪些库和表
			*.* 前*用来指定数据库名 后*指定表名
			to 将权限赋予某个用户
			jack@'localhost' jack用户 @后接限制的主机，可以是ip、ip段、域名、%  %表示任何地方
			identified by 指定用户的登录密码
			with grant option	表示此用户可以将拥有的权限授权给别人
			
			flush privileges 刷新权限 使权限生效
			show grants 查看权限
			show grants for 'jack'@'%'; 查看某个用户
			revoke delete on*.* from jack'@'localhost  回收权限
			drop user 'jack'@'localhost'  删除用户
			rename user 'jack'@'%' to 'jim'@'%'  对账户重命名
			
			
			
			
#### 内存配置相关参数
		1.sort_buffer_size：排序缓冲区大小，这个参数定义了每个线程所使用的排序缓冲区的大小，当查询请求需要排序时，MySQL服务器会立即分配给链接这个参数所定义大小的缓冲区的全部内存。而不管这个排序是否需要这么大的内存，如果把这个参数设置成100M，那么10个需要排序查询的链接就会占用1G的内存，因此这个参数的配置要格外小心，不要将这个参数的值设置的过大。
		2.join_buffer_size：这个参数定义的是MySQL的每个线程所使用的连接缓冲去的大小，如果查询中关联了多张表，那么MySQL就会为每一个连接分配一个缓冲区，因此这个参数也不要设置的过大。在这里需要提醒一下，在互联网环境中，为了提升性能，尽量避免使用连表查询，尤其是大表的连表查询。
		3.read_buffer_size：这个参数是在MySQL进行全表扫描时所分配的内存的大小，这个参数的大小一定要是4K的倍数。
		4.read_rnd_buffer_size：索引缓冲区的大小，MySQL只是在需要时分配索引缓冲区，并且只会分配需要的内存的大小，不会按照参数设置的大小分配内存。
		以上四个参数都是为每个线程分配的，也就是说，如果有100个线程，那么所使用的内存就要×100，所以这些参数的配置值都不能过大，否则就可能找出内存浪费甚至溢出。
		5.innodb_buffer_pool_size：innodb存储引擎缓冲池大小，innodb缓冲池中缓存的数据页（默认16K）类型有：索引页、数据页、undo页、插入缓冲（合并多次写为一次写）、自适应哈希索引、锁信息、数据字典信息等。索引innodb存储引擎的性能严重依赖于这个参数，一般情况下，在系统允许的范围内，这个值应该设置的尽量大一些，计算公式如下：
		总内存-（每个线程所使用的内存×连接数）-系统保留内存。在MySQL的官方手册中建议将innodb_buffer_pool_size的大小设置为服务器内存的75%以上，但这要考虑实际情况，必须满足上面的公式的前提下才可以设置。
		从InnoDB1.0.x版本之后，引入了innodb_buffer_pool_instances参数，这个参数允许设置多个缓冲池实例，每个页根据哈希值平均分配到不同的缓冲池实例中。这样做的好处是减少数据库内部的资源竞争，增加数据库的并发处理能力。可以通过命令show variables like 'innodb_buffer_pool_instances'\G查看当前缓冲池实例个数。
#### IO相关配置参数
		innodb是基于事务的存储引擎，每次数据修改，innodb首先要将事务预写到事务日志中，然后再写入磁盘，而不是每次提交都写入磁盘，因为磁盘IO的性能比较差。
		1.innodb_log_file_size：单个事务日志大小
		2.innodb_log_files_in_group：innodb事务日志文件的数量
		事务日志的总大小=innodb_log_files_in_group×innodb_log_file_size，事务日志是循环写入的方式，如果事务比较繁忙，建议将innodb_log_file_size的值调整大一些，减少文件交换。事务日志应能保持数据库服务器近1-2个小时内的事务状况，这样有利于数据恢复。
		3.innodb_log_buffer_size：日志缓冲区大小，一般32M就足够用了。
		4.innodb_flush_log_at_trx_commit：该参数控制innodb事务日志的刷新频次，有三个值：
		0：每秒进行一次log写入cache，并flush log到磁盘；
		1：默认值，在每次事务提交执行log写入cache，并flush log到磁盘，这种配置最安全，但是性能低；
		2：建议使用这个值，每次提交事务，执行log写入cache，每秒执行一次flush log到磁盘。
		5.innodb_flush_method：innodb刷新的方式，建议使用O_DIRECT，关闭深度缓存。
		6.innodb_file_per_table：innodb如何使用表空间，如果设置为1，那么将为每个表建立一个独立的表空间，这里强烈建议设置该参数为1。
		7.innodb_doublewrite：开启innodb二次写，为了增加数据的安全性，该参数也强烈建议设置为1。
#### 安全相关参数
		1.expire_logs_days：指定自动清理binlog的天数，建议设置在7天左右。
		2.max_allowed_packet：控制MySQL可以接收的数据包的大小，建议改成32M。如果使用了主从复制，那么这个参数最好保持一致。
		3.sysdate_is_now：确保sysdate()返回确定性。
		4.read_only：禁止非super权限的用户写权限，建议在主从复制环境的从数据库上开启这个配置，以保证从数据库不会被误写。
		5.skip_slave_start：禁止slave自动恢复，建议在主从复制环境的从数据库上开启这个配置，以避免从数据库重启后自动启动负责。
#### 其他
		1.sync_binlog：控制MySQL如何向磁盘刷新binlog，主从复制环境，建议将主数据库设置为1
		2.tmp_table_size和max_heap_table_size：控制内存临时表的大小，这两个值应该设置相同值，而且不要太大。
		3.max_connections：最大连接数，默认是100，这个值太小了，建议改成2000及以上。

		
		
		
		
		
		
		[mysqld]
		user = mysql
		port = 3306
		socket = /data/3306/mysql.sock
		basedir = /usr/local/mysql
		datadir = /data/3306/data
		open_files_limit    = 10240

		back_log = 600   #在MYSQL暂时停止响应新请求之前，短时间内的多少个请求可以被存在堆栈中。如果系统在短时间内有很多连接，则需要增大该参数的值，该参数值指定到来的TCP/IP连接的监听队列的大小。默认值50。max_connections = 3000   #MySQL允许最大的进程连接数，如果经常出现Too Many Connections的错误提示，则需要增大此值。max_connect_errors = 6000   #设置每个主机的连接请求异常中断的最大次数，当超过该次数，MYSQL服务器将禁止host的连接请求，直到mysql服务器重启或通过flush hosts命令清空此host的相关信息。table_cache = 614  #指示表调整缓冲区大小。# table_cache 参数设置表高速缓存的数目。每个连接进来，都会至少打开一个表缓存。#因此， table_cache 的大小应与 max_connections 的设置有关。例如，对于 200 个#并行运行的连接，应该让表的缓存至少有 200 × N ，这里 N 是应用可以执行的查询#的一个联接中表的最大数量。此外，还需要为临时表和文件保留一些额外的文件描述符。# 当 Mysql 访问一个表时，如果该表在缓存中已经被打开，则可以直接访问缓存；如果#还没有被缓存，但是在 Mysql 表缓冲区中还有空间，那么这个表就被打开并放入表缓#冲区；如果表缓存满了，则会按照一定的规则将当前未用的表释放，或者临时扩大表缓存来存放，使用表缓存的好处是可以更快速地访问表中的内容。执行 flush tables 会#清空缓存的内容。一般来说，可以通过查看数据库运行峰值时间的状态值 Open_tables #和 Opened_tables ，判断是否需要增加 table_cache 的值（其中 open_tables 是当#前打开的表的数量， Opened_tables 则是已经打开的表的数量）。即如果open_tables接近table_cache的时候，并且Opened_tables这个值在逐步增加，那就要考虑增加这个#值的大小了。还有就是Table_locks_waited比较高的时候，也需要增加table_cache。external-locking = FALSE  #使用–skip-external-locking MySQL选项以避免外部锁定。该选项默认开启max_allowed_packet = 32M  #设置在网络传输中一次消息传输量的最大值。系统默认值 为1MB，最大值是1GB，必须设置1024的倍数。sort_buffer_size = 2M  # Sort_Buffer_Size 是一个connection级参数，在每个connection（session）第一次需要使用这个buffer的时候，一次性分配设置的内存。#Sort_Buffer_Size 并不是越大越好，由于是connection级的参数，过大的设置+高并发可能会耗尽系统内存资源。例如：500个连接将会消耗 500*sort_buffer_size(8M)=4G内存#Sort_Buffer_Size 超过2KB的时候，就会使用mmap() 而不是 malloc() 来进行内存分配，导致效率降低。#技术导读 http://blog.webshuo.com/2011/02/16/mysql-sort_buffer_size/#dev-doc: http://dev.mysql.com/doc/refman/5.5/en/server-parameters.html#explain select*from table where order limit；出现filesort#属重点优化参数join_buffer_size = 2M   #用于表间关联缓存的大小，和sort_buffer_size一样，该参数对应的分配内存也是每个连接独享。thread_cache_size = 300   # 服务器线程缓存这个值表示可以重新利用保存在缓存中线程的数量,当断开连接时如果缓存中还有空间,那么客户端的线程将被放到缓存中,如果线程重新被请求，那么请求将从缓存中读取,如果缓存中是空的或者是新的请求，那么这个线程将被重新创建,如果有很多新的线程，增加这个值可以改善系统性能.通过比较 Connections 和 Threads_created 状态的变量，可以看到这个变量的作用。设置规则如下：1GB 内存配置为8，2GB配置为16，3GB配置为32，4GB或更高内存，可配置更大。thread_concurrency = 8   # 设置thread_concurrency的值的正确与否, 对mysql的性能影响很大, 在多个cpu(或多核)的情况下，错误设置了thread_concurrency的值, 会导致mysql不能充分利用多cpu(或多核), 出现同一时刻只能一个cpu(或核)在工作的情况。thread_concurrency应设为CPU核数的2倍. 比如有一个双核的CPU, 那么thread_concurrency的应该为4; 2个双核的cpu, thread_concurrency的值应为8#属重点优化参数query_cache_size = 64M   ## 对于使用MySQL的用户，对于这个变量大家一定不会陌生。前几年的MyISAM引擎优化中，这个参数也是一个重要的优化参数。但随着发展，这个参数也爆露出来一些问题。机器的内存越来越大，人们也都习惯性的把以前有用的参数分配的值越来越大。这个参数加大后也引发了一系列问题。我们首先分析一下 query_cache_size的工作原理：一个SELECT查询在DB中工作后，DB会把该语句缓存下来，当同样的一个SQL再次来到DB里调用时，DB在该表没发生变化的情况下把结果从缓存中返回给Client。这里有一个关建点，就是DB在利用Query_cache工作时，要求该语句涉及的表在这段时间内没有发生变更。那如果该表在发生变更时，Query_cache里的数据又怎么处理呢？首先要把Query_cache和该表相关的语句全部置为失效，然后在写入更新。那么如果Query_cache非常大，该表的查询结构又比较多，查询语句失效也慢，一个更新或是Insert就会很慢，这样看到的就是Update或是Insert怎么这么慢了。所以在数据库写入量或是更新量也比较大的系统，该参数不适合分配过大。而且在高并发，写入量大的系统，建议把该功能禁掉。#重点优化参数（主库 增删改-MyISAM）query_cache_limit = 4M    #指定单个查询能够使用的缓冲区大小，缺省为1Mquery_cache_min_res_unit = 2k    #默认是4KB，设置值大对大数据查询有好处，但如果你的查询都是小数据查询，就容易造成内存碎片和浪费#查询缓存碎片率 = Qcache_free_blocks / Qcache_total_blocks * 100%#如果查询缓存碎片率超过20%，可以用FLUSH QUERY CACHE整理缓存碎片，或者试试减小query_cache_min_res_unit，如果你的查询都是小数据量的话。#查询缓存利用率 = (query_cache_size – Qcache_free_memory) / query_cache_size * 100%#查询缓存利用率在25%以下的话说明query_cache_size设置的过大，可适当减小;查询缓存利用率在80%以上而且Qcache_lowmem_prunes > 50的话说明query_cache_size可能有点小，要不就是碎片太多。#查询缓存命中率 = (Qcache_hits – Qcache_inserts) / Qcache_hits * 100%default-storage-engine = MyISAM
		#default_table_type = InnoDB
		thread_stack = 192K  #设置MYSQL每个线程的堆栈大小，默认值足够大，可满足普通操作。可设置范围为128K至4GB，默认为192KB。transaction_isolation = READ-COMMITTED   #设定默认的事务隔离级别.可用的级别如下:# READ-UNCOMMITTED, READ-COMMITTED, REPEATABLE-READ, SERIALIZABLE# 1.READ UNCOMMITTED-读未提交2.READ COMMITTE-读已提交3.REPEATABLE READ -可重复读4.SERIALIZABLE -串行tmp_table_size = 256M   # tmp_table_size 的默认大小是 32M。如果一张临时表超出该大小，MySQL产生一个 The table tbl_name is full 形式的错误，如果你做很多高级 GROUP BY 查询，增加 tmp_table_size 值。如果超过该值，则会将临时表写入磁盘。max_heap_table_size = 256M
		long_query_time = 2
		log_long_format
		log-slow-queries=/data/3306/slow-log.log
		#log-bin = /data/3306/mysql-bin
		log-bin
		binlog_cache_size = 4M
		max_binlog_cache_size = 8M
		max_binlog_size = 512M
		expire_logs_days = 7
		key_buffer_size = 2048M #批定用于索引的缓冲区大小，增加它可以得到更好的索引处理性能，对于内存在4GB左右的服务器来说，该参数可设置为256MB或384MB。read_buffer_size = 1M  # MySql读入缓冲区大小。对表进行顺序扫描的请求将分配一个读入缓冲区，MySql会为它分配一段内存缓冲区。read_buffer_size变量控制这一缓冲区的大小。如果对表的顺序扫描请求非常频繁，并且你认为频繁扫描进行得太慢，可以通过增加该变量值以及内存缓冲区大小提高其性能。和sort_buffer_size一样，该参数对应的分配内存也是每个连接独享。read_rnd_buffer_size = 16M   # MySql的随机读（查询操作）缓冲区大小。当按任意顺序读取行时(例如，按照排序顺序)，将分配一个随机读缓存区。进行排序查询时，MySql会首先扫描一遍该缓冲，以避免磁盘搜索，提高查询速度，如果需要排序大量数据，可适当调高该值。但MySql会为每个客户连接发放该缓冲空间，所以应尽量适当设置该值，以避免内存开销过大。bulk_insert_buffer_size = 64M   #批量插入数据缓存大小，可以有效提高插入效率，默认为8Mmyisam_sort_buffer_size = 128M   # MyISAM表发生变化时重新排序所需的缓冲myisam_max_sort_file_size = 10G   # MySQL重建索引时所允许的最大临时文件的大小 (当 REPAIR, ALTER TABLE 或者 LOAD DATA INFILE).# 如果文件大小比此值更大,索引会通过键值缓冲创建(更慢)myisam_max_extra_sort_file_size = 10G
		myisam_repair_threads = 1   # 如果一个表拥有超过一个索引, MyISAM 可以通过并行排序使用超过一个线程去修复他们.# 这对于拥有多个CPU以及大量内存情况的用户,是一个很好的选择.myisam_recover   #自动检查和修复没有适当关闭的 MyISAM 表skip-name-resolve
		lower_case_table_names = 1
		server-id = 1innodb_additional_mem_pool_size = 16M   #这个参数用来设置 InnoDB 存储的数据目录信息和其它内部数据结构的内存池大小，类似于Oracle的library cache。这不是一个强制参数，可以被突破。innodb_buffer_pool_size = 2048M   # 这对Innodb表来说非常重要。Innodb相比MyISAM表对缓冲更为敏感。MyISAM可以在默认的 key_buffer_size 设置下运行的可以，然而Innodb在默认的 innodb_buffer_pool_size 设置下却跟蜗牛似的。由于Innodb把数据和索引都缓存起来，无需留给操作系统太多的内存，因此如果只需要用Innodb的话则可以设置它高达 70-80% 的可用内存。一些应用于 key_buffer 的规则有 — 如果你的数据量不大，并且不会暴增，那么无需把 innodb_buffer_pool_size 设置的太大了innodb_data_file_path = ibdata1:1024M:autoextend   #表空间文件 重要数据innodb_file_io_threads = 4   #文件IO的线程数，一般为 4，但是在 Windows 下，可以设置得较大。innodb_thread_concurrency = 8   #服务器有几个CPU就设置为几，建议用默认设置，一般为8.innodb_flush_log_at_trx_commit = 2   # 如果将此参数设置为1，将在每次提交事务后将日志写入磁盘。为提供性能，可以设置为0或2，但要承担在发生故障时丢失数据的风险。设置为0表示事务日志写入日志文件，而日志文件每秒刷新到磁盘一次。设置为2表示事务日志将在提交时写入日志，但日志文件每次刷新到磁盘一次。innodb_log_buffer_size = 16M  #此参数确定些日志文件所用的内存大小，以M为单位。缓冲区更大能提高性能，但意外的故障将会丢失数据.MySQL开发人员建议设置为1－8M之间innodb_log_file_size = 128M   #此参数确定数据日志文件的大小，以M为单位，更大的设置可以提高性能，但也会增加恢复故障数据库所需的时间innodb_log_files_in_group = 3   #为提高性能，MySQL可以以循环方式将日志文件写到多个文件。推荐设置为3Minnodb_max_dirty_pages_pct = 90   #推荐阅读 http://www.taobaodba.com/html/221_innodb_max_dirty_pages_pct_checkpoint.html# Buffer_Pool中Dirty_Page所占的数量，直接影响InnoDB的关闭时间。参数innodb_max_dirty_pages_pct 可以直接控制了Dirty_Page在Buffer_Pool中所占的比率，而且幸运的是innodb_max_dirty_pages_pct是可以动态改变的。所以，在关闭InnoDB之前先将innodb_max_dirty_pages_pct调小，强制数据块Flush一段时间，则能够大大缩短 MySQL关闭的时间。innodb_lock_wait_timeout = 120   # InnoDB 有其内置的死锁检测机制，能导致未完成的事务回滚。但是，如果结合InnoDB使用MyISAM的lock tables 语句或第三方事务引擎,则InnoDB无法识别死锁。为消除这种可能性，可以将innodb_lock_wait_timeout设置为一个整数值，指示 MySQL在允许其他事务修改那些最终受事务回滚的数据之前要等待多长时间(秒数)innodb_file_per_table = 0   #独享表空间（关闭）[mysqldump]
		quick
		max_allowed_packet = 32M
		[mysqld_safe]
		log-error=/data/3306/mysql_oldboy.err
		pid-file=/data/3306/mysqld.pid#补充#wait_timeout = 10   #指定一个请求的最大连接时间，对于4GB左右的内存服务器来说，可以将其设置为5-10。#skip_networking   #开启该选可以彻底关闭MYSQL的TCP/IP连接方式，如果WEB服务器是以远程连接的方式访问MYSQL数据库服务器的，则不要开启该选项，否则将无法正常连接。

		#log-queries-not-using-indexes将没有使用索引的查询也记录下来

## mysql相关

#### 查询速度
		 编写查询之前要明白，真正重要的是响应时间。
		 查询如果是一个任务，由一系列子任务组成，每个子任务会消耗一定的时间
		 优化查询就是优化子任务，要么消除其中一些子任务，要么减少子任务的执行次数，要么让子任务运行的更快
		 查询需要在不同的地方花费时间。包括网络、CPU计算、生成统计信息和执行计划、锁等待等
		
		 1、确认应用是否在检索大量超过需要的数据。（访问太多行或者太多列）
		 2、确认MYSQL服务器是否在分析大量超过需要的数据行
		 3、重复查询相同的数据
		 
		 一般情况下MYSQL能使用一下三种方式应用WHERE条件
			* 在索引中使用where条件来过滤不匹配的记录，在存储引擎层完成
			* 使用索引覆盖扫描来返回记录，直接从索引中过滤不需要的记录并返回命中的结果
			* 从数据表中返回数据，然后过滤不满足条件的记录。在mysql服务器层完成，mysql需要先从数据表中读出记录然后过滤

### 重构查询
		*一个复杂查询还是多个简单查询
			考虑是否需要将一个复杂查询分成多个简单查询
		*切分查询	
			有时需要将大查询切分成小查询，只完成一小部分，每次只返回一小部分查询结果
			如大量的数据删除就可以分批次删除，也可将服务器上原本的一次性压力分散到时间段中，降低对服务器的影响
		*分解关联查询
			优势:
				1、让缓存效率更高
				2、查询分解后，执行单个查询可以减少锁的竞争
				3、在应用层做关联，更容易对数据库进行拆分，更容易高性能、可扩展
				4、查询本身的效率也可能有所提升
				5、减少冗余记录的查询
				6、相当于在应用中实现了哈希关联、而不是使用mysql嵌套循环关联。
				
#### 查询缓存
		在解析一个查询语句之前，如果查询缓存是打开的，那么MYSQL会优先检查这个查询是否命中查询缓存中的数据
		这个检查是通过一个对大小写敏感的hash值来判定的。如果权限没有问题，mysql会跳过所有其他阶段，直接从缓存中拿到
		结果并返回给客户端
		
#### 查询优化处理
		语法解析器和预处理
			Mysql通过关键字将SQL语句进行解析，并生成一颗对应的'解析书'
			Mysql解析器将使用Mysql语法规则验证和解析查询
		查询优化器
			一条查询有多种执行方式，最后都返回相同的结果。优化器的作用是找到这其中最好的执行计划
			show status like 'last_query_cost';
				会返回valuie值表示需要多少个数据页的随机查找才能完成上面的查询
				根据表或者索引的页面个数、索引的基数、索引和数据行的长度、索引分布情况
				
#### 索引
		索引的类型
			B-Tree 索引
				如果没有特别指明类型，多半是B-Tree索引，用B-Tree数据结构来存储数据
			
			限制
				*如果不是按照索引的最左列开查找，则无法使用索引。
				*不能跳过索引中的列
				*如果查询中有某个列的查询范围，则其右边的所有列都无法使用索引优化查找

			哈希索引
				基于哈希表实现，只有精确匹配索引所有列的查询才有效
			限制
				* 哈希索引只包含哈希值和行指针，而不存储字段值，所以不能使用索引中的值来避免读行
				* 哈希索引数据并不是按照索引值顺序存储的，所以也就无法用于排序
				* 哈希索引页不支持部分索引列匹配查找，因为哈希索引始终是使用索引列的全部内容来计算哈希值的
				* 只支持等值的比较查询
				* 访问哈希索引的数据非常快，除非有很多哈希冲突
				* 如果哈希冲突很多的话，一些索引维护操作的代价也会很高。



























		
			
			
			
			
			
		









		
			
		