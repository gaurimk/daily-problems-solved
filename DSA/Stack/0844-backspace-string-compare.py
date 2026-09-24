class Solution:
    def backspaceCompare(self, s:str, t : str) -> bool:
        def removechr(string):
            stack = []
            for char in string:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack
        return removechr(s) == removechr(t)