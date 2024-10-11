class Solution(object):
    def smallestChair(self, times, targetFriend):
        list1 = []
        for i, ele in enumerate(times):
            list1.append((ele[0], ele[1], i))
        list1 = sorted(list1)


        used_chairs = [] #(endTime, chairnumber)
        available_chairs = [i for i in range(len(list1))]
        for st, end, person in list1:
            while(used_chairs and used_chairs[0][0] <= st):
                free_chair = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, free_chair[1])
            
            nearest_chair = heapq.heappop(available_chairs)
            heapq.heappush(used_chairs, (end, nearest_chair))
            if(person == targetFriend):
                return nearest_chair
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        
