class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        if len(pattern) != len(arr):
            return False
        dic = {}
        visited = set()
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]] != arr[i]:
                    return False
            elif arr[i] in visited:
                return False
            else:
                dic[pattern[i]] = arr[i]
                visited.add(arr[i])
        return True