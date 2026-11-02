class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for s_letter in s:
            if s_letter not in dict_s:
                dict_s[s_letter] = 1
            else:
                dict_s[s_letter] += 1
        for t_letter in t:
            if t_letter not in dict_t:
                dict_t[t_letter] = 1
            else:
                dict_t[t_letter] += 1
        if dict_s == dict_t:
            return True
        return False