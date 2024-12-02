class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        pre_mul = 1
        post_mul = 1

        for i in range(n):
            res[i]*= pre_mul
            pre_mul *= nums[i]
        
        for i in range(n-1,-1,-1):
            res[i] *= post_mul
            post_mul *= nums[i]

        return res 
        