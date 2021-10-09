class Dequeue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item==[]

    def addFront(self,item):
        return self.item.append(item)

    def addRear(self,item):
        return self.item.insert(0,item)

    def removeFront(self):
        return self.item.pop()
    def removeRear(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)
    def display(self):
        return self.item

dq = Dequeue()
print(dq.isEmpty())
dq.addFront(10)
dq.addFront(20)
dq.addRear(30)
dq.addRear(40)
dq.addFront(50)
dq.addRear(60)
print(dq.display())