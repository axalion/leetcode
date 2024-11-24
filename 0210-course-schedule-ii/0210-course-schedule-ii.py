from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        num_dependency = [0] * numCourses
        graph = defaultdict(list)
        num_course = 0

        if not prerequisites:
            return [i for i in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            num_dependency[course]+=1
        
        q = deque()

        for course in range(numCourses):
            if num_dependency[course] == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            res.append(course)
            num_course +=1

            for nei_node in graph[course]:
                num_dependency[nei_node] -= 1
                if num_dependency[nei_node] == 0:
                    q.append(nei_node)
            
        
        if num_course == numCourses:
            return res
        else:
            return [] 




        