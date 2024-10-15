class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            a = firstList[i]
            b = secondList[j]

            start = max(a[0], b[0])
            end = min(a[1], b[1])

            if start <= end:
                output.append([start, end])

            if a[1] < b[1]:
                i+=1
            else:
                j+=1
        
        return output
