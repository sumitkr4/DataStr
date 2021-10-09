class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head = node

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
            print(temp.data)
            temp=temp.next
    def get_length(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return  count
    def remove_at(self,index):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index ==0:
            self.head = self.head.next
        temp=self.head
        count = 0
        while temp.next:
            if count == index -1:
                temp.next=temp.next.next
                break
            temp=temp.next
            count+=1

    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")
        if index==0:
            self.insert_at_begining(data)
            return
        temp = self.head
        count=0
        while temp.next:
            if count ==index-1:
                node = Node(data,temp.next)
                temp.next= node
                break
            temp=temp.next
            count+=1

if __name__== '__main__':
    ll = LinkedList()
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_begining(30)
    ll.insert_at_begining(40)
    ll.insert_at_end(100)
    ll.remove_at(2)
    ll.insert_at(3,200)
    print(ll.get_length())
    ll.printElement()
