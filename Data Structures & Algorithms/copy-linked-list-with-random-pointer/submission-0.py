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
        old_nodes, new_nodes = [], []
        cur_node = head
        while cur_node is not None:
            print('0')
            old_nodes.append(cur_node)
            new_nodes.append(Node(cur_node.val, cur_node.next, cur_node.random))
            cur_node = cur_node.next
        for i in range(len(new_nodes)):
            print('1')
            if i < len(new_nodes) - 1:
                new_nodes[i].next = new_nodes[i + 1]
            else:
                new_nodes[i].next = None
            if old_nodes[i].random is None:
                new_nodes[i].random = None
            else:
                new_nodes[i].random = new_nodes[old_nodes.index(old_nodes[i].random)]
        if head is None:
            return head
        else:
            return new_nodes[0]
        
