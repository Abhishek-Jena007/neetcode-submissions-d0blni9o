class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        dictionary = dict()
        for num in nums:
            if num in dictionary:
                return True
            dictionary[num]= 1;
        return False
            