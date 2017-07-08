List = {}
function List.new()
	return {first = 0, last = -1}
end

function List.pushleft(list, value)
	local first = list.first - 1
	list.first = first
	list[first] = value
end

function List.pushright(list, value)
	local last = list.last + 1
	list.last = last
	list[last] = value
end

function List.popleft(list)
	local first = list.first
	if first > list.last then error("list is emtpy") end
	local value = list[first]
	list[first] = nil    -- to allow garbage collection
	list.first = first + 1
	return value
end

function List.popright(list)
	local last = list.last
	if list.first > last then error("list is empty") end
	local value = list[last]
	list[last] = nil
	list.last = last - 1
	return value
end


L = List.new()
List.pushleft(L, 1)
List.pushleft(L, 0)
List.pushright(L, 2)
List.pushright(L, 3)
List.popright(L)
List.popleft(L)

for i, v in pairs(L) do
	print(i,v)
end