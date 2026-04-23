class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checkDupli = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in checkDupli:
                checkDupli.remove(s[l])
                l += 1
            checkDupli.add(s[r])  # add()is a set method, only for set
            res = max(res,r-l+1 )
        return res
        
        
               