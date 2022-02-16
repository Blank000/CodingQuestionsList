class TrieNode:
    def __init__(self):
        self.child = {}
        
class Solution:
            
    def longestStrChain(self, words: List[str]) -> int:
        def chainCanBeCreated(a, b):
            if len(b) - len(a) != 1:
                return False
            idx = 0
            count = 0
            for i in range(len(b)):
                if count > 1:
                    return False
                if idx == len(a):
                    return True
                if b[i] == a[idx]:
                    idx += 1
                else:
                    count += 1
            return count == 1
        words.sort(key = len)
        dp = [1 for i in range(len(words))]
        dic = {}
        dic[0] = 0
        for i in range(len(words)):
            word = words[i]
            if len(word) not in dic:
                dic[len(word)] = i
            if len(word)-1 in dic:
                prevLenIdx = dic[len(word)-1]
                currLenIdx = dic[len(word)]
                for idx in range(prevLenIdx, currLenIdx):
                    if chainCanBeCreated(words[idx], word):
                        dp[i] = max(dp[i], dp[idx]+1)
        #print(dp, words, dic)
        return max(dp)
                    
            