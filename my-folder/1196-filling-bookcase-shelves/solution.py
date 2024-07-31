class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        cache = {}
        def helper(ind):
            if ind == len(books):
                return 0
            if ind in cache:
                return cache[ind]
            cur_width = shelfWidth
            max_height = 0
            cache[ind] = float("inf")
            for j in range(ind, len(books)):
                width, height = books[j]

                if(cur_width < width):
                    break
                
                cur_width -= width
                max_height = max(max_height, height)
                cache[ind] = min(cache[ind], helper(j + 1) + max_height)
            return cache[ind]
        return helper(0)
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        

# class Solution(object):
#     def minHeightShelves(self, books, shelfWidth):
#         tot_height = 0
#         def recursion(ind, width_available, cr_hieght):
#             #Base Case
#             if books[ind][0] > shelfWidth:
#                 return -1
#             if(books[ind][0] <= width_available):
#                 keep = 
            
#         tot_height += books[0][1]
#         recursion(1, shelfWidth-books[0][0])
        
#         """
#         :type books: List[List[int]]
#         :type shelfWidth: int
#         :rtype: int
#         """
        
