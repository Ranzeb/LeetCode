#https://leetcode.com/problems/group-anagrams/solutions/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        result = []
        for string in strs:
            sorted_str = sorted(string)
            sorted_str = ''.join(sorted_str)
            if sorted_str in dictionary.keys():
                dict_list = dictionary.get(sorted_str)
                dict_list.append(string)
            else:
                dictionary[sorted_str] = [string]
        

        for key, value in dictionary.items():
            result.append(value)
        
        return result