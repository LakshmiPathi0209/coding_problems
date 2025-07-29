from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        if not self.head:
            return "empty linked list"

        list_values = []
        pointer = self.head

        while pointer:
            list_values.append(str(pointer.val))
            pointer = pointer.next

        return "-->".join(list_values)

    @staticmethod
    def read_list(list_head):
        list_values = []
        pointer = list_head
        while pointer:
            list_values.append(pointer.val)
            pointer = pointer.next
        return list_values

    def append_list_value(self, value):

        if not self.head:
            self.head = ListNode(value)
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = ListNode(value)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list_l1 = LinkedList.read_list(l1)
        list_l2 = LinkedList.read_list(l2)
        list_l1.reverse()
        list_l2.reverse()
        l1_val = 0
        l2_val = 0
        res_val = []

        for i in list_l1:
            l1_val = l1_val * 10 + i
        for i in list_l2:
            l2_val = l2_val * 10 + i

        res = l1_val + l2_val
        if res == 0:
            temp = LinkedList()
            temp.append_list_value(0)
            return temp.head
        else:
            while res:
                res_val.append(res % 10)
                res = res // 10

            res_ll = LinkedList()
            for i in res_val:
                res_ll.append_list_value(i)
            return res_ll.head