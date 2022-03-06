class Solution:
	def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
		k = [(ages[i], scores[i]) for i in range(len(ages))]
		k.sort()
		dp = [k[i][1] for i in range(len(ages))]
		#print(k)
		for i in range(1,len(k)):
			for j in range(i):
				if k[j][0] < k[i][0]:
					if k[j][1] <= k[i][1]:
						dp[i] = max(dp[i], k[i][1] + dp[j])
				else:
					dp[i] = max(dp[i], k[i][1] + dp[j])
		#print(dp)
		return max(dp)

