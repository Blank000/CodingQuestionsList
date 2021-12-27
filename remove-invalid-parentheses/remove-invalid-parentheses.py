class Solution:
    
    def __init__(self):
        self.minm = float("inf")
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # For any point of time the number of closing brackets must be less than the number of opening brackets
        possibleAns = set()
        def recurse(idx, s, temp, op, cl, rem):
            if idx == len(s):
                if op == cl:
                    if rem <= self.minm:
                        if rem < self.minm:
                            possibleAns.clear()
                            self.minm = rem
                        possibleAns.add("".join(temp))
            else:
                if s[idx] == "(":    
                    recurse(idx+1, s, temp+[s[idx]], op+1, cl, rem)
                elif s[idx] == ")" and cl < op:
                    recurse(idx+1, s, temp+[s[idx]], op, cl+1, rem)
                elif s[idx] != ")" and cl <= op:
                    recurse(idx+1, s, temp+[s[idx]], op, cl, rem)
                if s[idx] == "(" or s[idx] == ")":
                    recurse(idx+1, s, temp, op, cl, rem+1)
        recurse(0, s, [], 0, 0, 0)
        return list(possibleAns)