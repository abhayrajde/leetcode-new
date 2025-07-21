class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        def firstMPrimes(n, m):
            primes = []
            for i in range(2, n + 1):
                if isPrime(i):
                    primes.append(i)
                    if len(primes) == m:
                        break
            return primes

        # BELOW SOL IS DP MEMOIZATION BUT MEMORY LIMIT EXCEEDS
        # THERE ARE SOME TWEEKS THAT CAN BE DONE FOR GENERATING FIRST M PRIME NUMBERS
        # TO TACKLE THE MEMORY ISSUE - DONE ABOVE    
        def isPrime(num):
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
            
        primes = firstMPrimes(n, m)

        dp = {}
        def dfs(ind, currSum):
            if currSum == n:
                return 0
            if ind >= len(primes) or currSum > n:
                return float('inf')
            
            if currSum in dp:
                return dp[currSum]
            
            notPick = dfs(ind + 1, currSum)
            pick = 1 + dfs(ind, currSum + primes[ind])
            
            dp[currSum] = min(pick, notPick)
            return dp[currSum]
        res = dfs(0,0)
        return res if res != float('inf') else -1
        

        
