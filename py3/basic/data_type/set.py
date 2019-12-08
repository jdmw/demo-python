set = {1,2,3}
print(set)

set = {x**2 for x in set}
print(set)

set = { x  for x in range(10)}
print(set)
set = {x**2 for x in range(10)}
print(set)
set = [x**2 for x in range(10) if x % 2 == 0]
print(set)


set = {x**2 for x in [1,2,1]}
print(set)


