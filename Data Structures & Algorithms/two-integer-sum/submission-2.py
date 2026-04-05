class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        add_list = list()
        for i in range(0,len(nums)):    # as we have to return the index we will 
            remain = target - nums[i]   # use i and range insted of val and no range
            
            if nums[i] in add_list:
                return [add_list.index(nums[i]),i]
            add_list.append(remain)
        