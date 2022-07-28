class TimeMap(object):

    def __init__(self):
        self.map = {} #key : [[value, timestamp]]
        
        
    def set(self, key, value, timestamp):
        if(key not in self.map):
            self.map[key] = []
        self.map[key].append([value,timestamp])
        
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        

    def get(self, key, timestamp):
        res = ""
        values = self.map.get(key, [])
        
        #Binary Search
        
        l = 0
        r = len(values)-1
        
        while(l<=r):
            m = (l+r)//2
            if(values[m][1] == timestamp):
                return(values[m][0])
            elif(values[m][1]>timestamp):
                r = m-1
            else:
                res = values[m][0]
                l = m+1
        return(res)
        
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
