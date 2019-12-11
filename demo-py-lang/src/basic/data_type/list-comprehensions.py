list = [x**3 for x in range(10)]
print(list)

list = [x**3 for x in range(10) if(x%2 ==0)]
print(list)

list = [(x+1,y+1) for x in range(3) for y in range(3) if(x!=y)]
print(list)

matrix = [[row*4+col for col in range(4)] for row in range(3)]
print(matrix)