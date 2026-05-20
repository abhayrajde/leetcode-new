class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA, setB = set(), set()
        counter = 0
        res = []

        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])

            if A[i] == B[i]:
                counter += 1
            elif B[i] in setA and A[i] in setB:
                counter += 2
            elif B[i] in setA or A[i] in setB:
                counter += 1

            res.append(counter)
        return res



