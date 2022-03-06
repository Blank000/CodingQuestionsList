class Solution:
	def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
		combined = sorted(zip(startTime, endTime, profit))
		startTime.sort()
		nextJob = {idx : bisect.bisect_left(startTime, combined[idx][1]) for idx in range(len(startTime)) }
		@lru_cache(None)
		def recurse(idx):
			if idx == len(startTime):
				return 0
			return max(recurse(idx+1), combined[idx][2] + recurse(nextJob[idx]))
		return recurse(0)
        


