class Solution(object):
    def removeSubfolders(self, folder):
        dict1 = defaultdict(list)
        s = list()
        list1 = []
        res = []
        flag = False
        for fldr in folder:
            count = fldr.count("/")
            list1.append((fldr,count))
        list1 = sorted(list1, key = lambda x:x[1])
        for i in list1:
            curr, count = i
            temp = curr.split("/")
            temp = temp[1:]
            for j in range(len(temp)):
                temp1 = temp[:j+1]
                if temp1 in s:
                    flag = True
                    break
            if not flag:
                s.append(temp)
                res.append(curr)
            flag = False
        return res

            



            
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        
