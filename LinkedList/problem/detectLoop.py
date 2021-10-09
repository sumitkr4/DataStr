class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        temp = self.head
        while temp.next:
            temp=temp.next
        temp.next = Node(data,None)

    def printElement(self):
        if self.head is None:
            print("Linked list is empty")
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

    def detectLoop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False

if __name__== '__main__':
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_end(100)
    ll.printElement()
    ll.detectLoop()