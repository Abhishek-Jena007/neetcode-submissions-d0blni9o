class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            remain = target - i
            if remain in numbers:
                index_remain = numbers.index(remain)
                break
            else:
                continue
        op_list = [numbers.index(i)+1,index_remain+1]
        return op_list
        