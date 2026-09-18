class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = []
        negative = []
        result = []
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result