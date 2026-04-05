class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        add_list = list()
        for i in range(0,len(nums)):
            remain = target - nums[i]
            
            if nums[i] in add_list:
                return [add_list.index(nums[i]),i]
            add_list.append(remain)
        