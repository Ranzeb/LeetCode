#https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for num in nums:
            if num in dictionary.keys():
                tmp = dictionary[num]
                tmp += 1
                dictionary[num] = tmp
            else:
                dictionary[num] = 1

        idx = 0
        max = 0
        
        result = []

        for i in range(0,k):
            for key, elm in dictionary.items():
                if elm > max:
                    max = elm
                    idx = key
            dictionary[idx] = 0
            result.append(idx)
            max = 0
            idx = 0

        return result
        