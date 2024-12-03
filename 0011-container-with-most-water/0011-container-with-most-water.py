class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        l,r = 0,n-1

        while l < r:
            ht = min(height[l],height[r])
            wd = r - l
            area = wd * ht
            max_area = max(area, max_area)

            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        
        return max_area



        