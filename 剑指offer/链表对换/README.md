'''
1->2->3->4转换成2->1->4->3
'''

class ListNose:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapParis(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapParis(next.next)
            next.next = head
            return next
        return head
