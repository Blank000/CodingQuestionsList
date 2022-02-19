class Solution:
    def __init__(self):
        self.inc = 0
        
    def minNumberOperations(self, target: List[int]) -> int:
        # First we will increase the whole array with 1 number then we are gonna have to see which number indices are fulfilled
        prev = 0
        inc = 0
        for i in range(len(target)):
            if target[i] <= prev:
                prev = target[i]
                continue
            if target[i] > prev:
                inc += target[i]-prev
            prev = target[i]
        return inc