class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[i])
        
        memo = {0: nums[0], 1: max(nums[0], nums[1])}

        def max_loot(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i]+ max_loot(i-2), max_loot(i-1))
                return memo[i]

        
        return max_loot(n-1)

        