class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        self.n = n
        return self.helper(self.n, self.memo)
        
    def helper(self, n, memo):    
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n in memo.keys():
            return memo[n]
        memo[n] = self.helper(n-1,memo) + self.helper(n-2, memo)
        return memo[n]
    
    def recursive_climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)