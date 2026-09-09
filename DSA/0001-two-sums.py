class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        n = len(nums)
        for i in range(n):
            arr.append([nums[i], i])
        arr.sort()
        left, right = 0 , n - 1
        while left < right:
            sum1 = arr[left][0] + arr[right][0]
            if sum1 == target:
                return [arr[left][1] , arr[right][1]]
            elif sum1 < target:
                left += 1
            else:
                right -= 1
        return []

        