from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_count = Counter(nums)
        sorted_dict = dict(sorted(f_count.items(), key = lambda x: x[1], reverse = True))

        keys  = list(sorted_dict.keys())
        return keys[:k]