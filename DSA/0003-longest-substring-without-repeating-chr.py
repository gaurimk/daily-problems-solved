class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        maxlen = 0
        charset = set()
        for right in range(n):
            if s[right] in charset:
                charset.add(s[right])
                maxlen = max(maxlen , right - left + 1)
            else:
                while s[right] in charset:
                    charset.remove(s[left])
                    left += 1
                charset.add(s[right])
        return maxlen