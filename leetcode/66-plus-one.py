class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_over = 1
        for i in range(len(digits) - 1, -1, -1):
            cur_digit = digits[i] + carry_over
            if cur_digit < 10:
                digits[i] = cur_digit
                return digits
            elif i == 0 and cur_digit >= 10:
                digits[i] = 0
                digits.insert(0, carry_over)
                return digits
            elif cur_digit >= 10:
                digits[i] = 0

