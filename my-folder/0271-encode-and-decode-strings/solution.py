class Codec:

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        

    def decode(self, s):
        res = []
        i = 0
        while(i < len(s)):
            j = i
            while(s[j] != "#"):
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j+1+length
        return res

        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
