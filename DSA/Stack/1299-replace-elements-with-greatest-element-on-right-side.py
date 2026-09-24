class Solution:
    def replaceElements(self,arr:List[int]) -> List[int]:
        stack = []
        n = len(arr)
        for i in range(n - 1 , -1, -1):
            current = arr[i]
            if not stack:
                arr[i] = -1
                stack.append(current)
            else:
                arr[i] = stack[-1]
                stack.append(max(current, stack[-1]))
        return arr
                