class BSTNode(object):
    def __init__(self, key,valuestr=None,value=1, left=None, right=None):
        self.key = key
        self.value = value
        self.valuestr = valuestr
        self.left = left
        self.right = right
 
    #def add(self, node):
    #    if node.valuestr < self.valuestr:
    #       if self.left is None:
    #          self.left = node
    #       else:
    #           self.left.add(node)
    #    else:
    #        if self.right is None:
    #            self.right = node
    #        else:
    #            self.right.add(node)
class BTS:
    def __init__(self):
        self.root = None
        self.size = 0
        self. node = BSTNode(self)
        
    def achar(self,node):
        if self.root is None:
            self.root = node
        else:
            if str(node.valuestr) < str(self.valuestr):
                if self.left is not None:
                    self.left = achar(node)
                else:
                    self.left = node

            elif str(node.valuestr) > str(self.valuestr):
                if self.right is not None:
                    self.right = achar(node)
                else:
                    self.right = node
            else:
                self.value += 1
            
    def percorrer(self):
        if self.left is None:
            if self.right is None:
              return
            else:
                print(self.right)
                self.right = percorrer()
        else:
            print(self.left)
            self.left = percorrer()
            
    def traverse(rootnode):
        thislevel = [rootnode]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print(n.value,n.key),
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            print()
            thislevel = nextlevel
              
          

mortos = []
bts = BTS()
ass,mort = input().split()
node = BSTNode(ass)
pri = ass
mortos.append(mort)
bts.achar(node)
while(True):
    try:
      ass,mort = input().split()
      node = BSTNode(ass)
      mortos.append(mort)
      bts.achar(node)
    except KeyboardInterrupt:
      print(bts.percorrer())
      node.traverse()
      break

