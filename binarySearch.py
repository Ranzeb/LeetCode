#https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1
        out = -1
        while left_idx <= right_idx:
            middle = (right_idx + left_idx) // 2
            curr_value = nums[middle]
            if curr_value == target:
                out = middle
                return out
            elif target > curr_value:
                left_idx = middle + 1
            else:
                right_idx = middle - 1

        return out 