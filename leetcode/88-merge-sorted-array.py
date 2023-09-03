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

# O(m+n) time O(1) space
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        for p in range(m + n - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1