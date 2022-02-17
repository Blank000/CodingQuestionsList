class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Seems like a backtracking problem to me
        res = []
        def backTrack(candidates, target, temp, visited):
            if target < 0:
                return
            if target == 0:
                temp.sort()
                if tuple(temp) not in visited:
                    res.append(temp)
                    visited.add(tuple(temp))
            for i in range(len(candidates)):
                temp.append(candidates[i])
                backTrack(candidates, target-candidates[i], temp[:], visited)
                temp.pop()
        candidates.sort()
        temp = []
        visited = set()
        backTrack(candidates, target, temp, visited)
        return res