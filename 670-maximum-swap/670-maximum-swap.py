class Solution:
    def maximumSwap(self, num: int) -> int:
        # Maintaing a maximum from the right to left and doing a string comparison will help
        num = list(str(num))
        maxm = [len(num)-1]
        for i in range(len(num)-2, -1, -1):
            maxmUntilNow = int(num[maxm[0]])
            if int(num[i]) > maxmUntilNow:
                maxm = [i]+maxm
            else:
                maxm = [maxm[0]] + maxm
        #print(maxm)
        for i in range(len(num)):
            if maxm[i] != i and int(num[i]) < int(num[maxm[i]]):
                num[i], num[maxm[i]] = num[maxm[i]], num[i]
                #print(i, maxm[i], num)
                break
        return int("".join(num))