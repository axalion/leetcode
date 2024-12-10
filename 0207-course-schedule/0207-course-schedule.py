# from collections import defaultdict, deque
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = defaultdict(list)
#         course_visited = 0
#         num_depencies = [0] * numCourses

#         for course, prereq in prerequisites:
#             graph[prereq].append(course)
#             num_depencies[course] += 1
#         q = deque()

#         for i in num_depencies:
#             if num_depencies[i]==0:
#                 q.append(i)

#         while q:
#             course = q.popleft()
#             course_visited +=1

#             for nei_node in graph[course]:
#                 num_depencies[nei_node]-= 1
#                 if num_depencies[nei_node] == 0:
#                     q.append(nei_node)


#         return course_visited == numCourses






# # 1 - >4
# # 2 - > 4
# '''
# 1 - > 4
# 2 - > 4
# 3 - > 1
# 3 - > 2

# 1: 4
# 2: 4
# 3: 1, 2

# independent course  = 4

# 1 2
# 3



# '''



from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the graph and calculate the number of dependencies
        graph = defaultdict(list)
        num_dependencies = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            num_dependencies[course] += 1

        # Step 2: Initialize the queue with courses that have no prerequisites
        q = deque()
        for course in range(numCourses):
            if num_dependencies[course] == 0:
                q.append(course)

        # Step 3: Process the courses in the queue
        courses_visited = 0
        while q:
            course = q.popleft()
            courses_visited += 1

            for neighbor in graph[course]:
                num_dependencies[neighbor] -= 1
                if num_dependencies[neighbor] == 0:
                    q.append(neighbor)

        # Step 4: If all courses are visited, return True, else return False
        return courses_visited == numCourses




        