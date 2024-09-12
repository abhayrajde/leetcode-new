class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set()
        result = len(words)
        for i in range(len(allowed)):
            allowed_set.add(allowed[i])
        for i in range(len(words)):
            for char in words[i]:
                if(char not in allowed_set):
                    result -= 1
                    break
        return result
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        
