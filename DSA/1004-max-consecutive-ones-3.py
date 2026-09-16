class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,maxlen,zerocount = 0, 0 , 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zerocount += 1
            while zerocount > k:
                if nums[left] == 0:
                    zerocount -= 1
                left += 1
            maxlen = max(maxlen, right - left + 1)
        return maxlen