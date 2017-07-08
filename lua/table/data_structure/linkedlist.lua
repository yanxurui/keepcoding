-- init an empty linked list
head = nil

-- insert a node at the head
node = {value = 1}
if head then
	node.next = head
    head.previous = node
    head = node
else
	head = node
end

-- insert a node at the rear
local rear = head
while rear and rear.next do
  rear = rear.next
end
node = {value = 2}
if rear then
	node.previous = rear
	rear.next = node
else
	rear = node
end


-- insert a node before node p
p = node
node = {next = p, previous = p.previous, value = 3}
if p.previous then
	p.previous.next = node
end
p.previous = node

-- traverse the list
local l = head
while l do
  print(l.value)
  l = l.next
end
