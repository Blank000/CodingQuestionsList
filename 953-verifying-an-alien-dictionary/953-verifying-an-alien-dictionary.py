class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def checkIsLexoSorted(w1, w2, priority):
            found = False
            for i in range(min(len(w1), len(w2))):
                if priority[w1[i]] > priority[w2[i]]:
                    return False
                elif priority[w1[i]] < priority[w2[i]]:
                    found = True
                    break
            return found or len(w1) <= len(w2)
        priority = {}
        count = 1
        for s in order:
            priority[s] = count
            count += 1
        for i in range(1, len(words)):
            if not checkIsLexoSorted(words[i-1], words[i], priority):
                return False
        return True