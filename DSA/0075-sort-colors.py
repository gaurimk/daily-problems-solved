class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        arr = sorted(nums)
        n = len(nums)
        mid = (n + 1) // 2
        small = arr[:mid][::-1]
        large = arr[mid:][::-1]
        for i in range(n):
            if i % 2 == 0:
                nums[i] = small[i//2]
            else:
                nums[i] = large[i//2]