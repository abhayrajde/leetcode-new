class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endofword = False
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofword = True
            
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endofword
        
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        
        curr = self.root
        
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
