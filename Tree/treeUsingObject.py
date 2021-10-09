class BinaryTree(object):
    def __init__(self,rootObject):
        self.key = rootObject
        self.leftChild = None
        self.rightChild =None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self,newObj):
        self.key=newObj

erer