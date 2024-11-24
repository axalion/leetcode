from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        p_cords = deque()
        p_seen = set()
        
        a_cords = deque()
        a_seen = set()

        for j in range(n):
            p_cords.append((0,j))
            p_seen.add((0,j))
        
        for i in range(1,m):
            p_cords.append((i,0))
            p_seen.add((i,0))
        
        for i in range(m):
            a_cords.append((i, n-1))
            a_seen.add((i, n-1))
        
        for j in range(n-1):
            a_cords.append((m-1,j))
            a_seen.add((m-1,j))
        
        def find_cords(q, seen):
            cords = set()

            while q:
                row, col = q.popleft()
                cords.add((row, col))

                for row_off, col_off in [(0,1), (0, -1), (1,0), (-1, 0)]:
                    nei_row, nei_col = row + row_off, col + col_off

                    if 0 <= nei_row < m and 0 <= nei_col < n and heights[nei_row][nei_col] >= heights[row][col] and (nei_row, nei_col) not in seen:
                        q.append((nei_row, nei_col))
                        seen.add((nei_row, nei_col))

            return cords


        p_set = find_cords(p_cords, p_seen)
        a_set = find_cords(a_cords, a_seen) 

        return list(p_set.intersection(a_set))


