# O(n) time O(1) space (since there are a limited number of valid characters)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in range(len(s)):
            if hashmap.get(s[i]) is None:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
        for i in range(len(t)):
            if hashmap.get(t[i]) is None:
                return False
            elif hashmap[t[i]] <= 0:
                return False
            else:
                hashmap[t[i]] -= 1
        return True