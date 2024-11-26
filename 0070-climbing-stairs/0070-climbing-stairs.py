class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def dp_memo(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = dp_memo(n-1) + dp_memo(n-2)
                return memo[n]
        return dp_memo(n)
        