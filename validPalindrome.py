#https://leetcode.com/problems/valid-palindrome/submissions/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_idx = 0
        right_idx = len(s) - 1

        while left_idx < right_idx:
            if s[right_idx].isalnum() == False:
                right_idx-=1
                continue
            if s[left_idx].isalnum() == False:
                left_idx+= 1
                continue

            if s[left_idx].lower() != s[right_idx].lower():
                return False
            else: 
                right_idx-=1
                left_idx+=1
        
        return True
