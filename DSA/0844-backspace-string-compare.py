class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def removechar(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack
        return removechar(s) == removechar(t)