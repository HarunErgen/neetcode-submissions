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
        old_to_new = dict()

        def copy_node(n):
            n_copy = None
            if n in old_to_new:
                n_copy = old_to_new[n]
            else:
                n_copy = Node(n.val, n.next, n.random)
                old_to_new[n] = n_copy


            next_copy = None
            if n.next and n.next in old_to_new:
                next_copy = old_to_new[n.next]
            elif n.next:
                next_copy = Node(n.next.val, n.next.next, n.next.random)
                old_to_new[n.next] = next_copy
            
            random_copy = None
            if n.random and n.random in old_to_new:
                random_copy = old_to_new[n.random]
            elif n.random:
                random_copy = Node(n.random.val, n.random.next, n.random.random)
                old_to_new[n.random] = random_copy
            
            n_copy.next = next_copy
            n_copy.random = random_copy

            return n_copy


        p = head
        while p:
            copy_node(p)
            p = p.next
        
        return old_to_new.get(head)