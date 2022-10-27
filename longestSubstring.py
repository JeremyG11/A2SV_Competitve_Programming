class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        start, end, longestString = 0, 0, 0
        distinct_char = set()
        while end < len(s):
            if s[end] not in distinct_char:
                distinct_char.add(s[end])
                end += 1
                longestString = max(longestString, len( distinct_char))
            else:
                distinct_char.remove(s[start])
                start += 1
        return longestString