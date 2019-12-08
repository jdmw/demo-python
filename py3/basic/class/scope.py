var1 = 1
def outside():
    #global var1
    var2 = 2 
    def inside():
        var3 = 3
        print('var1=',var1)
        print('var2=',var2)
        print('var3=',var3)
    print(var2)
    inside()
outside()