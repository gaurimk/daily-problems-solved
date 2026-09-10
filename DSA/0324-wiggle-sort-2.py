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


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort()
        mid = (n -1) // 2
        nums[::2],nums[1::2] = nums[mid::-1],nums[:mid:-1]