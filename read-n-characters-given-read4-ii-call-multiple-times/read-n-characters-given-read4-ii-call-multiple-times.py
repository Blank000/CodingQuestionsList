# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    
    def __init__(self):
        self.temp = []
        
    def read(self, buf: List[str], n: int) -> int:
        m = n - len(self.temp)
        if m <= 0:
            for i in range(n):
                buf[i] = self.temp[i]
            self.temp = self.temp[n:]
            return n
        else:
            for i in range(len(self.temp)):
                buf[i] = self.temp[i]
                idx = i 
            d = m - m%4
            r = m%4
            idx = len(self.temp)
            while d >= 4 and idx < d:
                buf4 = [""]*4
                read4(buf4)
                for i in range(4):
                    buf[idx+i] = buf4[i]
                idx += 4
            if idx < n:
                buf4 = [""]*4
                read4(buf4)
                for i in range(r):
                    buf[idx+i] = buf4[i]
                self.temp = buf4[r:]
            return n