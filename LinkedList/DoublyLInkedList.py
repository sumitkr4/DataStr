class doublyLinkedList(object):
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

a=doublyLinkedList(1)
b=doublyLinkedList(2)
c=doublyLinkedList(3)

a.next=b
b.prev=a
b.next=c
c.prev=b