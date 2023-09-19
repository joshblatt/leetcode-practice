# O(n) time O(1) space
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # ballon
        # 1 x b, 1 x a, 2 x l, 2 x o, 1 x n
        num_b = 0
        num_a = 0
        num_l = 0
        num_o = 0
        num_n = 0
        for ch in text:
            if ch == 'b':
                num_b += 1
            elif ch == 'a':
                num_a += 1
            elif ch == 'l':
                num_l += 1
            elif ch == 'o':
                num_o += 1
            elif ch == 'n':
                num_n += 1
        num_balloons = 0
        while True:
            if any(num <= 0 for num in (num_b, num_a, num_n)) or any(num <= 1 for num in (num_l, num_o)):
                return num_balloons
            else:
                num_b -= 1
                num_a -= 1
                num_l -= 2
                num_o -= 2
                num_n -= 1
                num_balloons += 1
