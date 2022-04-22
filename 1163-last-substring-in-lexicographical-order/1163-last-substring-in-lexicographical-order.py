class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i, j, k = 0, 1, 0
        while j+k < n:
            if s[i+k] == s[j+k]:
                k += 1
            elif s[i+k] < s[j+k]:
                i = max(i+k+1, j)
                j, k = i+1, 0
            else:
                j += k+1
                k = 0
        return s[i:]
                
'''
        int n=s.length(),i=0,j=1,k=0;
        while(j+k<n)
        {
            if(s[i+k]==s[j+k]) k++; 
            else if(s[i+k]<s[j+k]) i=max(i+k+1,j),j=i+1,k=0;
            else j+=k+1,k=0;
        }
        return s.substr(i);
'''