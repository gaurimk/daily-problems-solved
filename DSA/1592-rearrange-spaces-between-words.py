class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(' ')
        if len(words) == 1:
            return words[0] + ' ' * spaces
        gaps = len(words) - 1
        space_between = spaces // gaps
        extra_spaces = spaces % gaps
        return (' ' * space_between).join(words) + ' ' * extra_spaces