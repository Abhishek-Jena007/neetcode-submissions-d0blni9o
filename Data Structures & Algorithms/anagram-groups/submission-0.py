class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op_dict = {}
        for s in strs:
            count = [0]* 26 #creating a list of 26 0s
            for c in s:
                count[ord(c)- ord("a")] += 1
            key = tuple(count) # key should be hashable, hence list is typecated to tuple
            if key not in op_dict:
                op_dict[key] = []
            op_dict[key].append(s)
        return list(op_dict.values()) # as the  return type should be list of a list having strings
                                      # hence a list is made while returning

        