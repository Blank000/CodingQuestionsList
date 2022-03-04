class Solution:
	def change(self, amount: int, coins: List[int]) -> int:
		prev = [0]*(amount + 1)
		prev[0] = 1
		for i in range(len(coins)):
			curr = [0]*(amount+1)
			for j in range(amount+1):
				if j >= coins[i]:
					curr[j] += curr[j-coins[i]]
				curr[j] += prev[j]
			prev = curr
		return prev[-1]
