#### 查询重复出现次数最多的记录
	group by 语句用于结合聚合函数，根据一个或多个列对结果集进行分组
	SELECT phone,count(*) as count
		FROM phone_code
		GROUP BY phone
		ORDER BY count desc
		limit 10
		

	用一条SQL 语句 查询出每门课都大于80 分的学生姓名
	
	select name from stu group by name where id<100 having min(grade)>80
		group by name 通过名字分组 
		having min()/count()/max()  分组=》相同的名字 拥有的最大/最小/总数 + 条件
		where是聚合前的筛选，having是聚合后对筛选
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		