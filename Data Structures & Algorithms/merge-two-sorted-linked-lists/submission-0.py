# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        dummy = ListNode()
        output = dummy

        while curr1 is not None or curr2 is not None:
            if curr1 is None:
                print("1")
                output.next = curr2 
                output = output.next
                curr2 = curr2.next
                continue

            elif curr2 is None:
                print("2")
                output.next = curr1
                output = output.next
                curr1 = curr1.next
                continue

            elif curr1.val <= curr2.val:
                output.next = curr1
                curr1 = curr1.next

            else:
                output.next = curr2
                curr2 = curr2.next

            output = output.next
        
        # output.next = curr1 or curr2
        return dummy.next
