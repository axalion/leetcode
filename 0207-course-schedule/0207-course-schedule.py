from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        course_visited = 0
        num_depencies = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            num_depencies[course] += 1
        q = deque()

        for i in num_depencies:
            if num_depencies[i]==0:
                q.append(i)
        print(graph)

        while q:
            course = q.popleft()
            course_visited +=1

            for nei_node in graph[course]:
                num_depencies[nei_node]-= 1
                if num_depencies[nei_node] == 0:
                    q.append(nei_node)


        return course_visited == numCourses



            






        