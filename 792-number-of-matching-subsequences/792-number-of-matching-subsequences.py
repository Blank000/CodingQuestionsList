class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # This has a very unique answer as LCS is giving TLE
        dic = collections.defaultdict(list)
        for w in words:
            dic[w[0]].append(w)
        count = 0
        for i in range(len(s)):
            listOfWords = dic[s[i]]
            dic[s[i]] = []
            while listOfWords:
                word = listOfWords.pop()
                if len(word) == 1:
                    count += 1
                else:
                    #print(dic)
                    dic[word[1]].append(word[1:])
        return count
    
        