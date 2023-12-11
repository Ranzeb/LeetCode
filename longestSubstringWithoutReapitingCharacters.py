#https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        best_size = 0

        l, r = 0,1
        
        for r in range(len(s)):
            curr_char = s[r]
            if curr_char not in seen:
                best_size = max(best_size, r - l + 1)
            else:
                if seen[curr_char] < l:
                    best_size = max(best_size, r - l + 1)
                else:
                    l = seen[curr_char] + 1
            seen[curr_char] = r
        return best_size