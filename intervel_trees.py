class Node:
    def __init__(self, range= None, max= None):
        self.low= range[0]
        self.high= range[1]
        self.max= range[1]
        self.left= None
        self.right= None
class Interval_tree:
    def __init__(self):
        self.root= None
    def get_root(self):
        return self.root
    def add(self, range):
        if self.root==None:
            self.root= Node(range)
        else:
            self._add(range, self.root)
    def _add(self, range, node):
        node.max= range[1] if range[1]>node.max else node.max
        if range[0] < node.low:
            if(node.left != None):
                self._add(range, node.left)
            else:
                node.left = Node(range)
        else:
            if(node.right != None):
                self._add(range, node.right)
            else:
                node.right = Node(range)
    def find(self, range):
        if self.root!= None:
            self._find(self.root, range)
        else:
            return None	
    def _find(self, node, range):
        if range[0]==node.low and range[1]== node.high:
            return node
        elif range[0]<node.min and node.left!= None:
            self._find(node.left, range)
        elif range[0]>node.min and node.right!= None:
            self._find(node.right, range)	
    def printTree(self):
        if self.root != None:
            self._printTree(self.root)
    def _printTree(self, node):
        if node != None:
            self._printTree(node.left)
            print "low: "+str(node.low) + ' '+"high: "+ str(node.high)+' '+"max: "+str(node.max)+'   ',
            self._printTree(node.right)					
    def delete(self, key):
        if self.root!=None:
            self._delete(self.root,key)
        else:
            return None
    def _delete(self, node, key):
        global temp
        if node == None: 
               return None
        elif node.low == key[0] and node.high==key[1]:
            if node.left is None and node.right is None: 
                if temp.low<node.low:
                    temp.right= None
                else:
                    temp.left= None
            elif node.left is None: 
                if temp.low<node.low:
                    temp.right= node.right
                else:
                    temp.left= node.right
            elif node.right is None: 
                if temp.low<node.low:
                    temp.right= node.left
                else:
                    temp.left= node.left
            else:
                current_node= node.right
                while current_node.left:
                    current_node= current_node.left
                if temp.low<node.low:
                    temp.right= current_node
                    current_node.left= node.left
                elif temp.low>node.low:
                    temp.left= current_node
                    current_node.right= node.right    
        temp= node
        node.max= node.high
        if key[0] < node.low: 
            self._delete(node.left,key)
        else: 
            self._delete(node.right,key)
    def maxify(self):
        if self.root!=None:
            self._maxify(self.root)
    def _maxify(self, node):
        if node!= None:
            if node.left== None and node.right==None:
                node.max= node.high
            elif node.left== None:
                if node.max<node.right.max:
                    node.max= node.right.max
            elif node.right== None:
                if node.max< node.left.max:
                    node.max= node.left.max
            else:
                a= node.left.max if node.left.max>node.right.max else node.right.max
                node.max= a if node.max<a else node.max
    def search(self, key):
        if self.root!=None:
            self._search(self.root,key)
    def _search(self, node, key):
        if node!= None:
            if key[0]>node.low and key[1]<node.high:
                print "search intervel is: "+str(node.low)+":"+str(node.high)
            elif key[0]<node.low and node.left!=None:
                self._search(node.left,key)
            elif key[0]>node.low and node.right!=None:
                self._search(node.right,key)
            elif node.left==None and node.right==None:
                print "Not Present"
            
tree = Interval_tree()
tree.add([15,20])
tree.add([10,30])
tree.add([5,20])
tree.add([12,15])
tree.add([17,19])
tree.add([30,40])
print "Intervel Tree: "
tree.printTree()
print "\n"
temp= tree.get_root()
tree.search([21,23])
tree.maxify()


