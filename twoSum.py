# https://leetcode.com/problems/two-sum/solutions/4168409/video-visualization-of-o-n-solution-using-a-hash-table/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)): 
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            else:
                map[nums[i]] = i