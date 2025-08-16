class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = ""
        max_len = 0

        for ch in s:
            if ch in current:
                index = current.index(ch)
                current = current[index + 1:] + ch
            else:
                current += ch

            max_len = max(max_len, len(current))

        return max_len