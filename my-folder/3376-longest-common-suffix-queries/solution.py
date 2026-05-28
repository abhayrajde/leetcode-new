class TrieNode:
    def __init__(self):
        self.children = {}
        self.ind = float('inf')
        self.minLen = float('inf')


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, ind):
        node = self.root
        if len(word) < node.minLen:
            node.minLen = len(word)
            node.ind = ind
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

            if len(word) < node.minLen:
                node.minLen = len(word)
                node.ind = ind
    
    def query(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return node.ind
            node = node.children[ch]
        return node.ind


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        for ind, word in enumerate(wordsContainer):
            trie.insert(word[::-1], ind)

        res = []

        for qword in wordsQuery:
            res.append(trie.query(qword[::-1]))
        return res
            

