class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]],i]
            keys[nums[i]] = i
            
        return None
        