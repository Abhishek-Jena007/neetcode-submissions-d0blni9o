class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        store = {}
        for val in nums:
            store[val] = 1 + store.get(val,0)

        pair = []
        for num, fr in store.items():   # Convert to list of pairs
            pair.append([fr,num])       # You flip the structure to [frequency, number] Why?
        pair.sort()                     # Because sorting works on the first element by default.

        res = []
        while len(res)< k:
            res.append(pair.pop()[1])
        
        return res
