# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        idealCandidate = 0
        for possibleCandidate in range(1, n):
            if knows(idealCandidate, possibleCandidate):
                idealCandidate = possibleCandidate
        if self.is_candidate(idealCandidate, n):
            return idealCandidate
        return -1
    
    def is_candidate(self, idealCandidate, n):
        for i in range(n):
            if i != idealCandidate and (not knows(i, idealCandidate) or knows(idealCandidate, i)):
                return False
        return True