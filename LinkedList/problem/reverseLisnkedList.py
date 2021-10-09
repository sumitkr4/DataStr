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
    def reverseList(self):
        curr=self.head
        prev = None
        next=None
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        head=prev
        temp=head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next


if __name__== '__main__':
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_end(100)
    # ll.printElement()
    ll.reverseList()