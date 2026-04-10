class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        count , max_cnt = 1 , 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i-1] == nums[i]-1 :
                count += 1
            else:
                count = 1
            max_cnt = max(max_cnt, count)
        return max_cnt