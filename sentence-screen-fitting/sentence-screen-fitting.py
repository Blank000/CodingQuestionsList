class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        totalSentenceLen = sum(len(sentence[i]) for i in range(len(sentence))) + len(sentence)-1
        def getNextIdx(sentence, idx, cols, totalSentenceLen):
            # numberOfSpacesTaken, nextIdx, numberOfSentences
            n = 0
            if cols < len(sentence[idx]):
                return (idx, 0)
            cols -= len(sentence[idx])
            idx += 1
            while idx < len(sentence) and cols >= (1+len(sentence[idx])):
                cols -= (1+len(sentence[idx]))
                idx += 1
            if idx == len(sentence):
                n += 1
            else:
                return (idx, n)
                
            n += cols // (1+totalSentenceLen)
            cols = cols % (1+totalSentenceLen)
            i = 0
            if cols < 1+len(sentence[0]):
                return (0, n)
            else:
                i = 1
                cols -= (1+len(sentence[0]))
                while i < len(sentence) and cols >= (1+len(sentence[i])):
                    cols -= (1+len(sentence[i]))
                    i += 1
            return (i, n)
        counter = 0
        idx = 0
        dic = {}
        for i in range(rows):
            if idx in dic:
                newIdx, n = dic[idx]
                idx = newIdx
                counter += n
            else:
                newIdx, n = getNextIdx(sentence, idx, cols, totalSentenceLen)
                dic[idx] = (newIdx, n)
                idx = newIdx
                counter += n
        return counter
                
                