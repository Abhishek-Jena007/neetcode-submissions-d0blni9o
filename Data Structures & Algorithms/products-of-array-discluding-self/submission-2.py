class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        for val in nums:
            if val == 0:
                continue
            mul *= val
        res = []
        count = 0
        for val in nums:
            if val == 0:
                count += 1
        if count >= 2:
            return [0]* len(nums)
        # try:
        for val in nums:
                if count == 1:
                    if val == 0:
                        res.append(int(mul))
                    else:
                        res.append(0)
                else:
                    res.append(int(mul/val)) 
        # except ZeroDivisionError:
        #     for val in nums:
        #         res.append(int(mul))
        return res
        