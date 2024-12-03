class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        h = {} # Num : Index
        seen = set()

        for i, val in enumerate(nums):
            h[val] = i

        for i in range(n):
            if i > 0 and nums[i]== nums[i-1]:
                continue
            for j in range(i+1,n):
                target = - nums[i] - nums[j]
                if target in h and h[target]!=i  and h[target]!=j:
                    seen.add(tuple(sorted([nums[i], nums[j], target])))
        
        return list(seen)


        