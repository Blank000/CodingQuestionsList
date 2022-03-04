class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		prev = [math.inf]*(amount+1)
		prev[0] = 0
		for i in range(len(coins)):
			curr = [math.inf]*(amount+1)
			curr[0] = 0
			for j in range(1,amount+1):
				if j < coins[i]:
					curr[j] = prev[j]
				else:
					curr[j] = min(prev[j], 1+curr[j-coins[i]])
			prev = curr
		return prev[-1] if prev[-1] != math.inf else -1
		
