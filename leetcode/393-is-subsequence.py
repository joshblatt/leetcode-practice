class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start_index = 0
        for i in range(len(s)):
            char_seen = False
            for j in range(start_index, len(t)):
                if s[i] == t[j]:
                    start_index = j + 1
                    char_seen = True
                    break
            if not char_seen:
                return False
        return True
