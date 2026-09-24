class Solution:
    def minAddToMakeValid(self, s:str) -> int:
        stack = []
        addition = 0
        for char in s:
            if char =='(':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    addition += 1
        return len(stack) + addition