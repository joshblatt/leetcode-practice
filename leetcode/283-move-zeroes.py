class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num_zeros
        p_first_zero = len(nums)
        for p_read in range(len(nums)):
            if nums[p_read] == 0:
                p_first_zero = p_read
            # if there is a non-zero number and a zero left of the non-zero number
            elif nums[p_read] != 0 and p_first_zero < p_read:
                # swap
                temp = nums[p_read]
                nums[p_read] = 0
                nums[p_first_zero] = temp
                p_first_zero = p_readv