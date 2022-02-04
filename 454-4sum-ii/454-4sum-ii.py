class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # In a generalised solution, I will create a dcitionary with sum of elements of arrays untill A and B, and then find the corresponding complements in C and D combined
        dic = {}
        lists = [A, B, C, D]
        def createHash(lists, dic, i, sum):
            if i == len(lists)//2:
                dic[sum] = dic.get(sum, 0) + 1
                return
            for a in lists[i]:
                createHash(lists, dic, i+1, sum+a)
        
        def countNumberOfComplements(lists, dic, i, sum):
            if i == len(lists):
                return dic.get(sum, 0)
            cnt = 0
            for a in lists[i]:
                cnt += countNumberOfComplements(lists, dic, i+1, sum-a)
            return cnt
        
        targetSum = 0
        createHash(lists, dic, 0, 0)
        return countNumberOfComplements(lists, dic, len(lists)//2, targetSum)
        
        