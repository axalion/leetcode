"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        o_to_n = {}

        start = head

        while start:
            o_to_n[start] = Node(start.val)
            start = start.next

        start = head
        while start:
            nei = start.next
            rand = start.random
            if nei:
                o_to_n[start].next = o_to_n[nei]
            if rand:
                o_to_n[start].random = o_to_n[rand]
            start = start.next
        
        return o_to_n[head]

        