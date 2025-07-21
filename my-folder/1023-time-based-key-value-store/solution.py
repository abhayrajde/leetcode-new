class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        
        list1 = self.hm[key]
        l, r = 0, len(list1) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if list1[mid][0] == timestamp:
                return list1[mid][1]

            if timestamp < list1[mid][0]:
                r = mid - 1
            else:
                res = list1[mid][1]
                l = mid + 1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
