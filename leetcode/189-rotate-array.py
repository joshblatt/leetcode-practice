# initial solution
# O(kn) time O(1) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums.pop()
            nums.insert(0, temp)

# initial array
# 1 2 3 4 5 6 7
# reverse all numbers
# 7 6 5 4 3 2 1
# reverse first k numbers (ie k = 3)
# 5 6 7 4 3 2 1
# reverse last k numbers
# 5 6 7 1 2 3 4
# O(n) time O(1) space
class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        