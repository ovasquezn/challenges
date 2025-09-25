"""
Problem: 2. Add Two Numbers (LeetCode, Medium)

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
Add the two numbers and return the result as a linked list.

You may assume the two numbers do not contain leading zeros,
except the number 0 itself.

-----------------------------------------------------
Examples:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

-----------------------------------------------------
Constraints:
- The number of nodes in each linked list is between 1 and 100
- 0 <= Node.val <= 9
- The input lists do not have leading zeros (except 0 itself)

-----------------------------------------------------
Approach:
- Traverse both linked lists node by node
- At each step, add corresponding digits plus any carry from the previous step
- Create a new node with the digit (total % 10) and update carry (total // 10)
- Continue until both lists and carry are fully processed
- Return the head of the resulting linked list

Time Complexity: O(max(m, n)), where m and n are the lengths of the lists
Space Complexity: O(max(m, n)), for the new linked list
"""


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next
    
# Example usage:
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))

l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output: 7 -> 0 -> 8