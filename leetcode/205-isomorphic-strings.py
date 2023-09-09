# O(n) time O(n) space
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s_to_t = {}
        map_t_to_s = {}
        for i in range(len(s)):
            if map_s_to_t.get(s[i]) is None and map_t_to_s.get(t[i]) is None:
                map_s_to_t[s[i]] = t[i]
                map_t_to_s[t[i]] = s[i]
            elif map_s_to_t.get(s[i]) is None or map_t_to_s.get(t[i]) is None:
                return False
            if map_s_to_t[s[i]] != t[i] or map_t_to_s[t[i]] != s[i]:
                return False
        return True