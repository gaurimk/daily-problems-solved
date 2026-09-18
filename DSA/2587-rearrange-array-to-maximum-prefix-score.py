class Solution:
    def maxScore(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        total = 0
        count = 0
        for num in nums:
            total += num
            if total > 0:
                count += 1
            else:
                break
        return count