"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # This is a kind of BFS traversal 
        dic = {}
        arr = []
        for e in employees:
            dic[e.id] = e
        arr = [id]
        def dfs(id):
            temp = []
            v = dic[id].importance
            for sid in dic[id].subordinates:
                v += dfs(sid)
            return v
        return dfs(id)