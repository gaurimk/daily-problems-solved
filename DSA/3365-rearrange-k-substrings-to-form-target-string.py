class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        size = n // k
        s_parts = []
        t_parts = []
        for i in range(0,n,size):
            s_parts.append(s[i:i+size])
            t_parts.append(t[i:i+size])
        s_parts.sort()
        t_parts.sort()
        return s_parts == t_parts