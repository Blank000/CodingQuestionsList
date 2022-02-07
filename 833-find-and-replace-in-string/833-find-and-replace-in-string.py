class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        l = list(s)
        for i, v in enumerate(indices):
            indices[i] = (v, i)
        indices.sort()
        for v, i in indices:
            source = sources[i]
            target = targets[i]
            if s[v:v+len(source)] == source:
                l[v] = target
                for j in range(v+1, v+len(source)):
                    l[j] = ""
        return "".join(l)