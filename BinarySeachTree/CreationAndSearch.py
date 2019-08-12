class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
                
def Search(root, key):  
    while root != None: 
 
        if key > root.val:  
            root = root.right 
            
        elif key < root.val: 
            root = root.left  
        else: 
            return True   
    return False
  
