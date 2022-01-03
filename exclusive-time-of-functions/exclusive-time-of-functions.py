from collections import defaultdict
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        st = []
        arr = [0]*n
        for i in range(len(logs)):
            
            p = logs[i].split(":")
            idx, time = int(p[0]), int(p[2])
            if p[1] == "end":
                _, start = st.pop()
                #print(idx, time, prevIdx, start)
                arr[idx] += time - start + 1
                if st:
                    prevIdx, t = st.pop()
                    st.append((prevIdx, time+1))
            else:
                if st:
                    lastJobStartTime = st[-1][1]
                    arr[st[-1][0]] += time - st[-1][1]
                st.append((idx, time))
            #print(st, arr)
        return arr