class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        n = len(arr)
        step = 2 * k
        for i in range( 0 , n , step):
            start = i
            end = min( i + k - 1 , n - 1)
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        return ''.join(arr)