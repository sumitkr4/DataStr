class QUsingStack:
    def __init__(self):
        self.inStack=[]
        self.outStack=[]

    def enqueue(self,item):
        return self.inStack.append(item)

    def dequeue(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append((self.inStack.pop()))
        return self.outStack.pop()

    def display(self):
        return self.inStack


qs=QUsingStack()
qs.enqueue(10)
qs.enqueue(20)
qs.enqueue(30)
qs.enqueue(40)
qs.enqueue(50)
print(qs.display())
print(qs.dequeue())