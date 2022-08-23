class Solution(object):
    def kClosest(self, points, k):
        distheap = []
        heapq.heapify(distheap)
        count = 0 
        for i in range(len(points)):
            dist = sqrt((points[i][0]**2) + points[i][1]**2)
            heapq.heappush(distheap,[-(dist),points[i][0],points[i][1]])
            count+=1
            if(count>k):
                heapq.heappop(distheap)
                count-=1
        res = []
        while(k>0):
            temp = heapq.heappop(distheap)
            res.insert(0,[temp[1],temp[2]])
            k-=1
        return res
                
        
        '''
        #TIME COMPLEXITY : O(N)+O(NLOGN)+O(K) - O(NLOGN)
        #SPACE COMPLEXITY : O(N)
        distheap = []
        for i in range(len(points)): #O(N)-TC
            dist = sqrt((points[i][0]**2) + (points[i][1]**2))
            distheap.append([dist,points[i][0],points[i][1]])
            
        heapq.heapify(distheap) #O(NLOGN) -TC
        res = []
        while(k>0): #O(K)
            temp = heapq.heappop(distheap)
            res.append([temp[1],temp[2]])
            k-=1
        return res
        '''
        '''
        #TIME COMPLEXITY : O(N)+O(NLOGN)+O(K)
        #SPACE COMPLEXITY : O(2N)
        dist = {}
        res = []
        for i in range(len(points)):    #O(N)
            eu_dist = (points[i][0]**2) + (points[i][1]**2)
            if(eu_dist not in dist):
                dist[eu_dist] = []
            dist[eu_dist].append(points[i])
        print dist
        temp = sorted(dist.items(), key = lambda x:x[0])    #O(NLOGN)
        print temp
        while(k>0):     #O(K)
            temp1 = temp.pop(0)
            for i in range(len(temp1[1])):
                if(k>0):
                    res.append(temp1[1][i])
                    k-=1
                else:
                    break
        return res
        '''
            
            
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
