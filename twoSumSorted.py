#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(numbers) - 1

        while left_idx < right_idx:
            sum = numbers[left_idx] + numbers[right_idx]
            if sum == target:
                return [left_idx + 1, right_idx + 1]
            
            if sum > target:
                right_idx -= 1
            else:
                left_idx += 1

        return []