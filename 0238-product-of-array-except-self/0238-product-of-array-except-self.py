class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left_product = [1] * n

        for i in range(1,n):
            left_product[i] *= left_product[i-1] * nums[i-1]
        right_product = 1
        for i in range(n-1,-1,-1):
            res[i] = left_product[i] * right_product
            right_product = right_product * nums[i]

        return res


        