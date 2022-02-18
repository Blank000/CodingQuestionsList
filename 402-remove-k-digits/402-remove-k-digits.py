class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        i = 0
        if len(num) == k:
            return "0"
        while k > 0 and i < len(num):
            n = num[i]
            if len(st) == 0:
                st.append(n)
                i += 1
            else:
                if n < st[-1]:
                    st.pop()
                    k -= 1
                else:
                    st.append(n)
                    i += 1
        if k != 0:
            return str(int("".join(st[:-k])))
        while i < len(num) and k == 0:
            n = num[i]
            st.append(n)
            i += 1
        
        return str(int("".join(st)))
                    