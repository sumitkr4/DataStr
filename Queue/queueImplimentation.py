class Queue:
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item==[]
    def enqueue(self,item):
        return self.item.insert(0,item)
    def dequeue(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
queue=Queue()
print(queue.isEmpty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue.dequeue())
print(queue.size())