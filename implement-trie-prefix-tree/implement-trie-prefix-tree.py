from collections import defaultdict

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {} # Character -> Node mapping
        #self.root = None

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        listofChildren = self.child # List of children of root
        for c in word:
            listofChildren[c] = listofChildren.get(c, {})
            listofChildren = listofChildren[c]
        listofChildren["#"] = listofChildren.get("#", {})
        
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        listofChildren = self.child # List of children of root
        for i in range(len(word)):
            if word[i] in listofChildren:
                listofChildren = listofChildren[word[i]]
            else:
                return False
        if "#" in listofChildren:
            return True
        return False

    def startsWith(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        listofChildren = self.child # List of children of root
        for i in range(len(word)):
            if word[i] in listofChildren:
                listofChildren = listofChildren[word[i]]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)