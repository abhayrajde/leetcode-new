class Solution(object):
    def numTeams(self, rating):
        dpinc = [[-1 for c in range(4)] for i in range(len(rating))]
        dpdec = [[-1 for c in range(4)] for i in range(len(rating))]
        teams = 0

        
        def recursion(ind, team_size, dp):
            # Base condition - reached end of array
            if ind == len(rating):
                return 0
            
            #Base condition: found a valid team of size 3
            if(team_size == 3):
                return 1

            if dp[ind][team_size] != -1:
                return dp[ind][team_size]

            valid_teams = 0
            for next_ind in range(ind+1, len(rating)):
                if rating[next_ind] > rating[ind]:
                    valid_teams += recursion(next_ind, team_size + 1, dp)
            
            dp[ind][team_size] = valid_teams
            return valid_teams
            
        for i in range(len(rating)):
            teams += recursion(i, 1, dpinc) 
        
        rating = rating[::-1]
        
        for i in range(len(rating)):
            teams += recursion(i, 1, dpdec) 

        return teams
        """
        :type rating: List[int]
        :rtype: int
        """
        
# class Solution(object):
#     def numTeams(self, rating):
#         dp = [[-1 for c in range(3)] for i in range(len(ratings))]
#         count = [0]
#         def recursion(ind, pairs):
#             # Base condition
#             if(pairs and len(pairs) == 3):
#                 count[0] += 1
#                 return
#             if ind >= len(rating):
#                 return
#             if(pairs):
#                 if(rating[ind] > pairs[-1]):
#                     pairs.append(rating[ind])
#                     take = recursion(ind+1, pairs)
#                     pairs.pop()
#             else:
#                 pairs.append(rating[ind])
#                 take = recursion(ind+1, pairs)
#                 pairs.pop()
#             not_take = recursion(ind+1, pairs)
#         recursion(0,[])

#         rating = rating[::-1]
#         recursion(0,[])

#         return count[0]
#         """
#         :type rating: List[int]
#         :rtype: int
#         """
        
