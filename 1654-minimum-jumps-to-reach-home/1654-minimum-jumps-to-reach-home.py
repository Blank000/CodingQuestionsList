class Solution:
	def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
		maxVal = 6000
		numOfSteps = [math.inf]*maxVal
		numOfSteps[0] = 0
		for i in forbidden:
			numOfSteps[i] = -1
		postn = deque()
		postn.append(0)
		while postn:
			position = postn.popleft()
			if position+a < maxVal and numOfSteps[position+a] > numOfSteps[position] + 1:
				numOfSteps[position+a] = numOfSteps[position] + 1
				postn.append(position+a)
			if position-b > 0 and numOfSteps[position-b] > numOfSteps[position] + 1:
				numOfSteps[position-b] = numOfSteps[position] + 1
				if position-b+a > 0 and position-b+a < maxVal and numOfSteps[position-b+a] > numOfSteps[position] + 2:
					postn.append(position-b+a)
					numOfSteps[position-b+a] = numOfSteps[position] + 2
		if numOfSteps[x] == math.inf:
			return -1
		return numOfSteps[x]
					

