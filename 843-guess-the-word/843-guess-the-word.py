# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import random
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def getPotentialCandidates(wordlist, n, baseWord, potentialCandidates):
            for word in wordlist:
                match = 0
                if word != baseWord:
                    for i in range(len(word)):
                        if word[i] == baseWord[i]:
                            match += 1
                    if match == n:
                        potentialCandidates.append(word)
        potentialCandidates = []
        word = random.choice(wordlist)
        n = master.guess(word)
        if n == 6:
            return
        getPotentialCandidates(wordlist, n, word, potentialCandidates)
        return self.findSecretWord(potentialCandidates, master)
    
    