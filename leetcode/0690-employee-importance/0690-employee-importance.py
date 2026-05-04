"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import deque

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp_map = {}
        for emp in employees:
            emp_map[emp.id] = (emp.importance, emp.subordinates)
        
        total = 0
        queue = deque([id])
        
        while queue:
            curr = queue.popleft()
            imp, subs = emp_map[curr]
            
            total += imp
            for s in subs:
                queue.append(s)
        
        return total
            