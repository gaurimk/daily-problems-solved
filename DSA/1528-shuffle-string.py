class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        pairs = list(zip(indices, s))
        pairs.sort()
        return ''.join([char for index, char in pairs])
    
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i, index in enumerate(indices):
            res[index] = s[i]
        return ''.join(res)