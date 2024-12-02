class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        n = len(nums)
        longest = 0

        for i in range(n):
            if nums[i]-1 not in seen:
                length = 1
                next_num = nums[i] + 1
                while next_num in seen:
                    next_num += 1
                    length+=1
                longest = max(longest, length)
        
        return longest


        