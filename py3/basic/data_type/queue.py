from collections import deque

queue = deque([1,2,3])
print(queue)

print('execute:append()')
queue.append(4)
print(queue)


print('execute:popleft()')
queue.popleft()
print(queue)


print('execute:popright()')
queue.pop()
print(queue)


