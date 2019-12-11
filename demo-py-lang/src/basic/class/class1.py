class Dog:
    kind = 'canine' 
    
    def __init__(self,name):
        self.name = name
        
    def printName(self):
        #nonlocal kind
        print('dog kind:',kind ,',name:',self.name)
        
        
#print(Dog('TiTi').kind)
Dog('TiTi').printName()