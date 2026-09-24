class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                inner = stack.pop()
                if inner == 0:
                    score = 0
                else:
                    score = 2 * inner
                stack[-1] += score
        return stack[0]