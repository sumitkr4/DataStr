class Stack:
    def __init__(self):
        self.item=[]

    def isEmpty(self):
        return self.item==[]
    def push(self,item):
        return self.item.append(item)
    def pop(self):
        return self.item.pop()
    def peak(self):
        return self.item[len(self.item)-1]
    def size(self):
        return len(self.item)
    def display(self):
        return self.item
stack = Stack()
print(stack.isEmpty())
stack.push('one')
stack.push('two')
stack.push('three')
stack.push('four')
stack.push('five')
print(stack.pop())
print(stack.peak())
print(stack.size())
print(stack.display())
