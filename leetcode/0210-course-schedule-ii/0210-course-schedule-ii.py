class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        next_course = [0 for _ in range(numCourses)]
        order = []
        # build graph
        for course, pre in prerequisites:
            graph[pre].append(course)
            #count next course edge
            next_course[course] += 1

        q = deque()
        #add the course in queue if degree 0
        for course in range(numCourses):
            if next_course[course] == 0:
                q.append(course)
        while q:
            course = q.popleft()
            order.append(course)

            #check neighbor
            for nei in graph[course]:
                next_course[nei] -= 1
                if next_course[nei] == 0:
                    q.append(nei)

        if len(order) != numCourses:
            return []

        return order

    
        