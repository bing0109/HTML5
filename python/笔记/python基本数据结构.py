https://www.jb51.net/article/113776.htm
Python入门_浅谈数据结构的4种基本类型


列表：list = [val1, val2, val3, val4]	中括号
字典：dict = {key1:val1, key2:val2}	大括号，且每个元素都带有冒号，key与val的对应关系组；
元组：tuple = (val1, val2, val3, val4)	小括号
集合：set = {val1, val2, val3, val4}	大括号



列表：
	1、特征
		a、元素可变
		b、列表中的元素都有序，即每个元素都有一个位置
		c、可以容纳python中的任何对象
	2、增
		list.insert(index, 'val')	新增元素到指定位置
		list.append('val')	新增元素到最后一位
		list.extend(list_b)	把list_b的元素扩展到list中

	3、删
		list.remove('val')
		list.pop()	删除最后一个元素
		del list[0:2]	删除index位0 1的元素
	4、改
		list[2]='val'	修改指定index的val
	5、查
		list[3]

	6、其他
		>>> a=[1,2,3,4,5]
		>>> a[::2]
		[1, 3, 5]
		# 字符串翻转
		>>> a[::-1]
		[5, 4, 3, 2, 1]
		>>> a[::1]
		[1, 2, 3, 4, 5]
		>>> a[::0]
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		ValueError: slice step cannot be zero
		>>> a[::3]
		[1, 4]
		>>> a[-2:]
		[4, 5]
		>>> a[::-2]
		[5, 3, 1]
		>>> a[::-3]
		[5, 2]
		>>> 
		>>> a
		[1, 2, 3, 4, 5]
		# 从第index=1位置，每2位取一个数字
		>>> a[1::2]
		[2, 4]
		# 一行代码实现对列表a中的偶数位置的元素进行加3后求和？
		>>> sum([i+3 for i in a if a.index(i)%2==0])

		# https://www.cnblogs.com/skiler/p/6959155.html



字典
	1、字典中的元素必须是 键值对 的形式
		key不可以重复，val可以重复
		key不可变，无法修改；val可修改，可以是任何对象
	2、增、改
		dict['key'] = 'value'	key在dict中不存在时，就属于新增，存在时就是修改
		dict.update({'key1':'value1', 'key2':'value2'})		效果同上，可以同时增、改多个

		eg：
			>>> dict = {'A':'art','B':'big','C':'cute'}
			>>> dict
			{'A': 'art', 'B': 'big', 'C': 'cute'}
			>>> dict['d'] = 'dcdec'
			>>> dict
			{'A': 'art', 'B': 'big', 'd': 'dcdec', 'C': 'cute'}
			>>> dict.update({'d':'abc','e':'efg'})
			>>> dict
			{'A': 'art', 'B': 'big', 'd': 'abc', 'C': 'cute', 'e': 'efg'}
			>>> 
			>>> dict['d'] = 'poiuy'
			>>> dict
			{'A': 'art', 'B': 'big', 'd': 'poiuy', 'C': 'cute', 'e': 'efg'}
			>>> 

	3、删除
		del dict['key']

		eg:
			>>> del dict['e']
			>>> dict
			{'A': 'art', 'B': 'big', 'd': 'poiuy', 'C': 'cute'}
			>>> 


	4、查
		dict['key']




元组
	tuple = (val1, val2, val3, val4)

	元组与列表类似，只是元组不可更改，只能查
	tuple[0]
	tuple[3:]


集合
	set={val1,val2,val3,val3}
	
	集合的概念有点接近于数学上的集合。每个集合中的元素是无序的、不重复的任何对象，我们可以通过集合去判断数据的从属关系，有时还可以通过集合把数据结构中重复的元素减掉。

	集合不可以被切片也不能被索引，除了做集合运算之外，集合元素可以被添加和删除。

	>>> set = {3,4,5,6,2,3,5,7}
	>>> set
	{2, 3, 4, 5, 6, 7}
	# 删除元素6
	>>> set.discard(6)
	>>> set
	{2, 3, 4, 5, 7}
	# 新增元素1
	>>> set.add(1)
	# 打印出的集合会从小到达排列，并去重
	>>> set
	{1, 2, 3, 4, 5, 7}
	>>> 



