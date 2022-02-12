class Solution:
    def ladderLength(self, beginWord: str, endWord: str, words: List[str]) -> int:
        dic = collections.defaultdict(list)
        for i in range(len(words)):
            dic[words[i]] = 1
        def bfs(level, temp, endWord, lengthOfBeginWord):
            if len(temp) == 0:
                return 0
            newTemp = set()
            for word in temp:
                for l in range(lengthOfBeginWord+1):
                    for i in range(97, 123):
                        newWord = word[:l-1]+chr(i)+word[l:]
                        #print(newWord)
                        
                        if newWord in dic:
                            if newWord == endWord:
                                return level + 1
                            newTemp.add(newWord)
                            del dic[newWord]
            #print(newTemp, level, dic)
            return bfs(level+1, newTemp, endWord, lengthOfBeginWord)
            
        temp = set()
        temp.add(beginWord)
        return bfs(1, temp, endWord, len(beginWord))
        