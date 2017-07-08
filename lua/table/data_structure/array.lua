-- ipairs函数会从1开始遍历，遇到一个nil值就停止
-- 遍历数组不要用pairs，因为table是无序的，用table实现的数组也是无序的
-- ipairs使用1,2,...作为健按顺序索引，而pairs使用一种无法预期的顺序索引
arr = {}
for i=1, 5 do
	arr[i] = i
end
arr[0] = 0
arr[10] = 10
for i,v in ipairs(arr) do
	print(i, v)
end

-- 使用constructors创建数组
-- 第一个元素的索引是1
arr = {1, '2', 3.0, false}
for i,v in ipairs(arr) do
	print(i, v)
end

x = 1
stack = {}
-- push
table.insert(stack, x)
-- pop
table.remove(stack)

queue = {}
-- enqueue
table.insert(queue, 1, x)
-- dequeue
table.remove(queue, x)
