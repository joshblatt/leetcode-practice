class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'0': 100000, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = 0
        prev = '0'
        for c in s:
            if values[prev] < values[c]:
                value += values[c] - 2 * values[prev]
            else:
                value += values[c]
            prev = c
        return value

