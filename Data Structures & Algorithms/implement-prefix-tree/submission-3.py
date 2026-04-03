class Node:
    
    def __init__(self, val, leaf):
        self.val = val
        self.leaf = leaf
        self.childs = {}

    def __str__(self):
        return f'({self.val}, {self.leaf})'


class PrefixTree:

    def __init__(self):
        self.root = Node('', False)

    def insert(self, word: str) -> None:
        cur_node = self.root
        for i in range(len(word)):
            leaf = i == len(word) - 1
            if word[i] not in cur_node.childs:
                cur_node.childs[word[i]] = Node(word[i], leaf)
            cur_node = cur_node.childs[word[i]]
            if leaf:
                cur_node.leaf = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        i = 0
        while cur_node and i < len(word):
            if word[i] not in cur_node.childs:
                return False
            cur_node = cur_node.childs[word[i]]
            i += 1
        return cur_node and cur_node.leaf

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        i = 0
        while cur_node and i < len(prefix):
            if prefix[i] not in cur_node.childs:
                return False
            cur_node = cur_node.childs[prefix[i]]
            i += 1
        return cur_node is not None
        
        