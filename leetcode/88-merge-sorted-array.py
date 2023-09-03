# O(m+n) time O(m) space
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        read_pointer1 = 0
        read_pointer2 = 0
        write_pointer = 0
        nums1_copy = nums1[:m]
        while write_pointer < m + n:
            if read_pointer2 >= n or (read_pointer1 < m and nums1_copy[read_pointer1] <= nums2[read_pointer2]):
                nums1[write_pointer] = nums1_copy[read_pointer1]
                read_pointer1 += 1
            else:
                nums1[write_pointer] = nums2[read_pointer2]
                read_pointer2 += 1
            write_pointer += 1