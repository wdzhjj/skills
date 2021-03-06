#### 关系型数据库 和 非关系型数据库
		RDBMS 
			高度组织化结构化数据
			结构化查询语言
			数据和关系都存储在单独表中
			数据操纵语言，数据定义语言
			严格的一致性
			基础事务
		NOSQL
			没有声明性查询语言
			没有预定义模式
			键值对存储、列存储、文档存储、图形数据库
			最终一致性，非ACID属性
			非结构化和不可预知的数据
			CAP定理
			高性能高可用可伸缩性

		CAP
			C consistenty 一致性  所有节点在同一时间具有相同的数据
			A availability  保证每个请求成功|失败都有响应
			P Partition tolerance	分隔容忍
				体统中任意信息的丢失|失败不影响系统的继续运作
		
		NOSQL 优缺点
			优点：
				高扩展、分布式计算、低成本、架构灵活、半结构化数据、无复杂关系
			缺点：
				没有标准化、有限的查询功能、不直观的程序
		

#### Redis | memcache | mongoDB 特点与区别
		Redis	
			优点：	
			1、支持多种数据结构
				string list dict(hash表) set zset(排序集合) hyperloglog(基数估算)
			2、支持通过replication 复制
				通过master-slave机制实时进行数据的同步复制，支持多级复制和增量复制
				主从机制是redis进行HA的重要手段
				HA(High Available) 高可用性集群
			3、支持持久化操作
				可进行 aof、rdb 数据持久化到磁盘，进行数据备份或数据恢复等操作，防止数据丢失
			4、单线程请求。所有命令串执行，并发情况不必考虑数据一致性
			5、支持pub|sub消息订阅机制
			6、支持简单事务需求
			缺点：
			1、单线程。性能受限于CPU，单实例最高5-6w QPS/s
			2、支持简单事务，场景少，不成熟
			3、string类型消耗较多内存，可以使用dict(hash表) 压缩存储以降低内存耗用
		
		Memcache
			优点：
				1、可利用多核优势，单实例吞吐量极高 几十万qps
				2、支持配置为 session handle
			缺点：
				1、只支持key|val 数据结构
				2、无法持久化，不能备份数据，重启后数据丢失
				3、无法进行数据同步，不能将MC中数据迁移到其他MC
				4、内存分配采用 Slab Allocation 机制管理内存
					value 大小分布差异较大时内存利用率降低，引发低利用率出踢出问题，要注重value设计
		
		MongoDB	
			优点：
				1、更高的写负载，插入速度快
				2、处理大规模的单表，容易分表
				3、高可用性，设置M-S不仅方便而且快，还可以快速安全自动化的实现节点故障转移
				4、快速的查询 MongoDB支持二维空间索引
				5、非结构化数据的增长，增加列在有些情况下回锁定整个数据库，或者增加负载导致性能下降
			缺点：
				1、不支持事务
				2、MongoDB占用空间过大
				3、没有成熟的维护工具
				
#### 三者的区别
			1、性能
				Memcache ≈ redis > mongoDB
			2、便利性
				memcache 结构单一
				redis丰富一些，数据操作方面更好
				mongodb 丰富的数据表达，索引，最类似关系型数据库，支持丰富的查询语言
			3、存储空间
				redis在2.0版本后增加的自己的 vm特性，突破物理内存的限制，可以对key|value支持过期时间
				memcache可修改最大可用内存，采用LRU算法
				MongoDB适合大数据量的存储，依赖系统的VM做内存管理，吃内存，不要和其他服务在一起
			4、一致性
				memcache在并发场景下，用 cas保证一致性
				redis 事务支持弱，只能保持事务中的每个操作连续执行
				mongo 不支持事务，内存数据分析的功能
			5、应用场景
				redis 数据量小的更多性能和操作和运算上
				memcache 用于动态系统中减少数据库负载，提升性能
						作缓存，提升性能 适合读多写少
				mongoDB 主要解决海量数据的访问效率问题
				
				
				
				
				
				
				
				
				
				
				
				
				
				






		