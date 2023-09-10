# double hash map solution to ensure uniqueness
# O(n) time O(n) space
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        pattern_to_s = {}
        s_to_pattern = {}
        for i in range(len(pattern)):
            if pattern_to_s.get(pattern[i]) is None and s_to_pattern.get(s[i]) is None:
                pattern_to_s[pattern[i]] = s[i]
                s_to_pattern[s[i]] = pattern[i]
            elif pattern_to_s.get(pattern[i]) is None or s_to_pattern.get(s[i]) is None:
                return False
            elif pattern_to_s[pattern[i]] != s[i]:
                return False
        return True