class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack = []
        greater = {}

        for i in nums2:

            while stack and i > stack[-1]:
                greater[stack.pop()] = i

            stack.append(i)

        while stack:
            greater[stack.pop()] = -1

        ans = []

        for i in nums1:
            ans.append(greater[i])

        return ans