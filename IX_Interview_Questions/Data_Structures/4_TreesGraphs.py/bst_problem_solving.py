# Source: http://interactivepython.org/courselib/static/pythonds/Trees/SearchTreeImplementation.html

class BinarySearchTree(object):
    def __init__(self):
        self.root = None 
        self.size = 0

    def length(self):
        return self.size 

    def __len__(self):
        return self.size 

    def __iter__(self):
        return self.root.__iter__()

    def put(self,key,val):
        """ Installs node in proper location in BST. """
        if self.root: # check if there is a root
            self._put(key,val,self.root) # call _put to install in proper location
        else: # declare new root
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        """ Searches BST for proper position and installs new node. """
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            # if there is no left child to search, we have found the location
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
        """ 
        With the put method, we can overload [] operator for assignment 
        like dictionaries with __setitem__

        ex: myZipTree['Plymouth'] = 55446
        """
        self.put(k,v)

    def get(self,key):
        """ Searches BST recursively; returns node object with given key. """
        if self.root:
            res = self._get(key,self.root)
            if res:
                   return res.payload
            else:
                   return None
        else:
            return None

    def _get(self,key,currentNode):
        """ Returns TreeNode for get; Uses same logic as _put """
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        """ 
        Make access items in BST like accessing a dictionary! 
        Ex: z = myZipTree['Plymouth'] returns 55446 
        """
        return self.get(key)

    def __contains__(self,key):
        """
        Using the get method, we can implement the in operation with __contains__
        """
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        
        else:
            raise KeyError('Error, key not in tree')
           

    def __delitem__(self, key):
        """ del operator for BST """
        self.delete(key)


    def remove(self, currentNode):
        """
        Assumes currentNode has parent (not the root). Handles bad news:
            1) Notifies parent that child is GONE
            2) Gives parent custody of its children if any. 
        
        3 cases:
        
        A) has parent and no children (leaf): 
            1) Just notify parents
        
        B) has parent and  2 children: 
            1) find successor: Successor always has at most 1 child.
            2) splice out: replace currentNode with successor so relations are OK
            aka, give parents custody of child (again, successor has at most 1 child)
        
        C) has parent and 1 child:
            1) give parent custody of child
        """
        
        if currentNode.isLeaf():
            if currentNode is currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else: # it is someone's right child
                currentNode.parent.rightChild = None
        
        elif currentNode.hasBothChildren:
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        
        else: # this node has 1 child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild(): 
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else: # has a left child but isn't anyone else's child -> root
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild) 
            
            else: # has a right child
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

    def findSuccessor(self):
        """ 
        Successor: smallest of right sub-tree. 
        1) Go to right sub-tree
        2) Go as far down left as possible. 
        * Smallest of the larger is successor
        """
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                    if self.isLeftChild():
                        succ = self.parent
                    else:
                        self.parent.rightChild = None
                        succ = self.parent.findSuccessor()
                        self.parent.rightChild = self
        return succ

    def findMin(self):
        """ Given a node, return most left node. Returns smallest in subtree """
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        """ Called on a successor, which has at most 1 child. """
        if self.isLeaf():
            # notify the parents
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            # Give grandparents custody
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


class TreeNode:
   def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self