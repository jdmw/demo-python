def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError as ze:
        # print("division by zero")
        print(ze)
        # raise ze 
    else:
        print(x,"/",y,"=",result)
    finally:
        print("executing finally clause")
        
        
divide(1,2)
divide(1,0)