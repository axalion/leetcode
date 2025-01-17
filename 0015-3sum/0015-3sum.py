class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l , r = i+1, n-1
            while l < r:
                if nums[l] + nums[r] == -val:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                elif nums[l] + nums[r] > -val:
                    r-=1
                else:
                    l+=1
                

        return res
                     

        