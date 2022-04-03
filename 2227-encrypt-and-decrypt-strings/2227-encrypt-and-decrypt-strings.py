class TrieNode:
    def __init__(self, val):
        self.val = val
        self.child = {}
    
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.dic = {}
        self.reverse_dic = collections.defaultdict(list)
        for i in range(len(keys)):
            self.dic[keys[i]] = values[i]
            self.reverse_dic[values[i]].append(keys[i])
        self.root = TrieNode("")
        for word in dictionary:
            self.add_to_trie(self.root, word)
        #print(self.root.child)

    def add_to_trie(self, node, word):
        if len(word) == 0:
            node.child["#"] = TrieNode("")
            return
        if word[0] not in node.child:
            node.child[word[0]] = TrieNode(word[0])
        self.add_to_trie(node.child[word[0]], word[1:])
        
    def encrypt(self, word1: str) -> str:
        res = []
        for i in range(len(word1)):
            res.append(self.dic[word1[i]])
        return "".join(res)

    def decrypt(self, word2: str) -> int:
        queueDic = collections.defaultdict(list)
        for val, child in self.root.child.items():
            queueDic[val].append(child)
        res  = 1
        for i in range(0, len(word2), 2):
            temp_dic = collections.defaultdict(list)
            if res == 0:
                return res
            key = word2[i:i+2]
            for val in self.reverse_dic[key]:
                if val in queueDic:
                    for node in queueDic[val]:
                        for val,child in node.child.items():
                            temp_dic[val].append(child)
            queueDic = temp_dic
        return len(queueDic["#"])
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)