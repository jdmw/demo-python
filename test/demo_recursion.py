

class Item :
    idx = 0
    child = None
    def __init__ (self,idx):
        self.idx = idx 
    

    def addChild(self,child):
        self.child = child 
    
    
    def __repr__(self):
        return "Item({})\n{}".format(self.idx, ("",str(self.child))[self.child != None]) 
    

root = Item(0)
latest = root 
cur = root 
for i in range(199) : 
     cur = Item(i+1)
     latest.addChild(cur)
     latest = cur

print(root)
#  conclude: maximum recursion depth = 200