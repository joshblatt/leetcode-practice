# brute force and ugly
# O(n^2) time O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the idea behind keeping track of the indices was to ensure that the min's index came before the max
        # but the nature of these nested loops wouldn't have allowed for that anyways
        # should have just tracked the max difference
        max_difference_indices = (None, None)
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if max_difference_indices is not (None, None):
                    if prices[j] - prices[i] > prices[max_difference_indices[1]] - prices[max_difference_indices[0]]:
                        max_difference_indices = (i, j)
                elif prices[j] > prices[i]:
                    max_difference_indices = (i, j)
                    
        if max_difference_indices is (None, None):
            return 0
        return prices[max_difference_indices[1]] - prices[max_difference_indices[0]]

# one pass
# keep track of the minimum price and maximum profit
# O(n) time O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit