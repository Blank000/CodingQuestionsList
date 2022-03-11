class Solution:
	def findIntegers(self, num: int) -> int:
		l = len(bin(num))-2
		def getCountOfNumberWithoutConsecutiveOnes(k):
			e0, e1 = 1, 0 # As we are starting with number 1, so we can only add 0 to it's last and not 1 ( to avoid consecutive ones )
			dp = [1]
			for i in range(1,k+1):
				dp.append(2*e0 + e1)
				e0, e1  = e0 + e1, e0
			return dp[k]
		countWithNumWithBinStringLengthSmaller = getCountOfNumberWithoutConsecutiveOnes(l-1) if (l > 1) else 0
		def checkIsNotConsecutive(num):
			isNotConsecutive = True
			isPrevOne = False
			while num:
				if num & 1:
					if isPrevOne:
						isNotConsecutive = False
						break
					isPrevOne = True
				else:
					isPrevOne = False
				num >>= 1
			return isNotConsecutive
		#print(countWithNumWithBinStringLengthSmaller)     
		n, count = 0, 0
		p = num
		while p :
			if p & 1 and checkIsNotConsecutive(p^1):
				count += getCountOfNumberWithoutConsecutiveOnes(n)
			p >>= 1
			if p == 1:
				break
			n += 1

		val = 0
		if checkIsNotConsecutive(num):
		    val = 1
		#print(isNotConsecutive, count, countWithNumWithBinStringLengthSmaller)
		return count + countWithNumWithBinStringLengthSmaller + val


