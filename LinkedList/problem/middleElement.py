###Logic only for finding meddile element of a linked list
def middleNode(self, ):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
