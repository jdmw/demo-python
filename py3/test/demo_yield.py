def createGenerator():
    for x in range(3) :
        yield x*10 

for i in createGenerator():
    print(i)