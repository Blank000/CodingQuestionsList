class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if digits == "":
            return []
        dic = {}
        dic["2"]= ["a","b","c"]
        dic["3"]= ["d","e","f"]
        dic["4"]= ["g","h","i"]
        dic["5"]= ["j","k","l"]
        dic["6"]= ["m","n","o"]
        dic["7"]= ["p","q","r","s"]
        dic["8"]= ["t","u","v"]
        dic["9"]= ["w","x","y","z"]
        def combo(digits, ans, res, idx):
            if idx == len(digits):
                ans.append("".join(res))
                return
            #for i in range(idx, len(digits)):
            value = dic[digits[idx]]
            for x in value:
                res.append(x)
                combo(digits, ans, res, idx+1)
                res.pop()
        
        combo(digits, ans, [], 0)
        return ans