'''
Find nth node of a linked list from end.
'''

## one method is we can find length of a linnked list and  find element at postition (len - n + 1)
'''
def printNthFromLast(self, n):
    temp = self.head  # used temp variable 

    length = 0
    while temp is not None:
        temp = temp.next
        length += 1

    # print count  
    if n > length:  # if entered location is greater  
        # than length of linked list 
        print('Location is greater than the' +
              ' length of LinkedList')
        return
    temp = self.head
    for i in range(0, length - n):
        temp = temp.next
    print(temp.data)

'''


## Another method

def nthElement(self,head,n):
    main_ptr = ref_ptr=head
    count=0
    if (head !=None):
        while count < n:
            if ref_ptr is None:
                print("n is greater then the number of element of list")
            ref_ptr=ref_ptr.next
            count+=1
    while ref_ptr is not None:
        ref_ptr=ref_ptr.next
        main_ptr=main_ptr.next
    print(main_ptr.val)
