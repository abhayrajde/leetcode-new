class Solution(object):
    def minimumPushes(self, word):
        hm = defaultdict(int)
        for let in word:
            hm[let] += 1

        sortedLets = sorted(hm.items(), key = lambda x: x[1], reverse = True)

        hm2 = {}
        count = 1
        place = 1
        for i in sortedLets:
            hm2[i[0]] = place
            count += 1
            if count == 9:
                count = 1
                place += 1
        count1 = 0
        for i in word:
            count1 +=hm2[i]
        return count1
             
            
        """
        :type word: str
        :rtype: int
        """
        
