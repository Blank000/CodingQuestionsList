class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # As the number of transactions are very small, the time complexity can go for exponential as well.
        # so we try all the posibilities of settling the debts with greedy and backtracking
        # +ve - Borrowed Money , -ve - Lend money
        debt = [0]*21
        for t in transactions:
            debt[t[0]] -= t[2]
            debt[t[1]] += t[2]
        arr = []
        for d in debt:
            if d != 0:
                arr.append(d)
        arr.sort()
        def greedyBackTrack(arr, idx):
            if idx == len(arr):
                return 0
            if arr[idx] == 0:
                return greedyBackTrack(arr, idx+1)
            length = float("inf")
            t1 = arr[idx]
            for j in range(idx+1, len(arr)):
                if arr[j] != 0 and arr[idx]*arr[j] < 0:
                    t2 = arr[j]
                    if arr[idx] < 0:
                        arr[idx] += min(-t1, t2)
                        arr[j] -= min(-t1, t2)
                        if arr[idx] == 0:
                            length = min(length, 1+greedyBackTrack(arr, idx+1))
                        else:
                            length = min(length, 1+greedyBackTrack(arr, idx))
                        arr[idx] = t1
                        arr[j] = t2
            return length
        return greedyBackTrack(arr, 0)
                        
                    