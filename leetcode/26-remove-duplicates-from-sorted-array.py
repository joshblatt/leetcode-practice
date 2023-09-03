# O(n) space is kinda bad but this works (tried to use same approach as last time)
# if it wasn't sorted this solution would still work however
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_seen = {}
        p_write = 0
        for p_read in range(len(nums)):
            # if number hasnt been seen
            if nums_seen.get(nums[p_read]) is None:
                # add to dict
                nums_seen[nums[p_read]] = True
                # write and increase writer
                nums[p_write] = nums[p_read]
                p_write += 1
        return p_write

            
# O(1) space
# works bc array is sorted
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_write = 1
        for p_read in range(1, len(nums)):
            # since array is sorted, repeating numbers will be next to each other
            # if not repeating
            if nums[p_read] != nums[p_read - 1]:
                # write and increase writer
                nums[p_write] = nums[p_read]
                p_write += 1
        return p_write

            
