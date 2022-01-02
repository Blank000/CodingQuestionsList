class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = collections.defaultdict(int)
        c = 0
        for i in range(len(time)):
            for k in range(1,17):
                if (60*k - time[i]) in dic:
                    print(60*k)
                    c += dic[60*k-time[i]]
            dic[time[i]] += 1
        return c