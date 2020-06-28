#### 查询重复出现次数最多的记录
	group by 语句用于结合聚合函数，根据一个或多个列对结果集进行分组
	SELECT phone,count(*) as count
		FROM phone_code
		GROUP BY phone
		ORDER BY count desc
		limit 10
		
