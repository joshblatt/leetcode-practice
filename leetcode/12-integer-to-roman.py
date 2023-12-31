class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [int(x) for x in str(num)]
        num_digits = len(digits)
        roman = ''
        letters = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        while num != 0:
            for divisor in letters:
                if floor(num / divisor) > 0:
                    roman += letters[divisor]
                    num -= divisor
                    break
        return roman


        

