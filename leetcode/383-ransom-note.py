# O(n) time O(n) space
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = {}
        for i in range(len(magazine)):
            if hm.get(magazine[i]) is None:
                hm[magazine[i]] = 1
            else:
                hm[magazine[i]] += 1
        for i in range(len(ransomNote)):
            # if not in magazine, return false
            if hm.get(ransomNote[i]) is None:
                return False
            # if ran out of letters, return false
            elif hm[ransomNote[i]] == 0:
                return False
            # decrease number of remaininig letters
            hm[ransomNote[i]] -= 1
        return True