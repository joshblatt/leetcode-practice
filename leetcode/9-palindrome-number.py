class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        digits = [int(i) for i in str(x)]
        for i in range(floor(len(digits) / 2)):
            if digits[i] != digits[-i - 1]:
                return False
        return True
