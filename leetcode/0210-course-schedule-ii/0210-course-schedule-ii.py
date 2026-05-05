class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        nextCourse = [0 for _ in range(numCourses)]
        order = []
        for course, pre in prerequisites:
           graph[pre].append(course)

        for node in range(numCourses):
            if nextCourse[node] != 0:
                continue
            if not self.topSort(node, nextCourse, graph, order):
                return []
        return list(reversed(order))
    def topSort(self, node, nextCourse, graph, order):
        if nextCourse[node] == 1:
            return False
        nextCourse[node] = 1
        for neighbor in graph[node]:
            if nextCourse[neighbor] == 2:
                continue
            if not self.topSort(neighbor, nextCourse, graph, order):
                return False
        # Color nodes black as we backtrack
        nextCourse[node] = 2
        order.append(node)
        return True