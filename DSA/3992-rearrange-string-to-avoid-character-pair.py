class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        result = []
        for char in s:
            if char == y:
                result.append(char)
        for char in s:
            if char != x and char != y:
                result.append(char)
        for char in s:
            if char == x:
                result.append(char)
        return ''.join(result)
            