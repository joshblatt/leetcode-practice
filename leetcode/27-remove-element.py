# read pointer iterates through entire array
# writer pointer increases only if current != val (ie needs to be in final array)
# note: when you see the a question saying "in-place" there is a good chance this strategy will work
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p_writer = 0
        for p_reader in range(len(nums)):
            if nums[p_reader] != val:
                nums[p_writer] = nums[p_reader]
                p_writer += 1
        return p_writer
                

