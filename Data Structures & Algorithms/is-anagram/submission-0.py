class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.lower()
        t.lower()
        s_dict=dict()
        t_dict = dict()
        for ch in s:
            s_dict[ch] = s_dict.get(ch,0) + 1
        for ch in t:
            t_dict[ch] = t_dict.get(ch,0) + 1
        if s_dict == t_dict:
            return True
        return False
        