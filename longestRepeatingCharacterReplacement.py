#https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        frequency = {}
        longest = 0

        for r in range(len(s)):
            if not s[r] in frequency:
                frequency[s[r]] = 0
            frequency[s[r]] += 1

            cells_count = r - l + 1
            
            if cells_count - max(frequency.values()) <= k:
                longest = max(longest, cells_count)
            else:
                frequency[s[l]] -= 1
                l += 1
        return longest