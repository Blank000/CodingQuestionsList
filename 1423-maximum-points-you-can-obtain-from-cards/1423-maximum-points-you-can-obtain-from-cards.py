class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        frontSum, backSum = 0, 0
        front, back = [], []
        for i in range(k):
            front.append(frontSum + cardPoints[i])
            frontSum = front[-1]
            back.append(backSum + cardPoints[-i-1])
            backSum = back[-1]
        maxPoints = max(front[k-1], back[k-1])
        for i in range(k-1):
            maxPoints = max(maxPoints, front[i]+back[k-2-i])
        return maxPoints