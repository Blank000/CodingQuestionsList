class Solution:
	def numberOfWeeks(self, milestones: List[int]) -> int:
		maxm = max(milestones)
		summ = sum(milestones)
		if maxm > summ-maxm:
			return 2*(summ-maxm) + 1
		return summ
