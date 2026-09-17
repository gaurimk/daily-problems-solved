class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left , maxlen , maxfreq = 0 , 0 , 0 
        count = {}
        for right in range(n):
            count[s[right]] = 1 + count.get(s[right],0)
            maxfreq = max(maxfreq , count[s[right]])
            windowlen = right - left + 1
            if windowlen - maxfreq > k:
                count[s[left]] -= 1
                left += 1
            maxlen = max(maxlen , right - left + 1)
        return maxlen