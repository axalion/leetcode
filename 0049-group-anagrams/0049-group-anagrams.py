class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}


        for word in strs:
            sorted_str = tuple(sorted(word))
            if sorted_str not in res:
                res[sorted_str] = []
            res[sorted_str].append(word)
        

        return list(res.values())

        