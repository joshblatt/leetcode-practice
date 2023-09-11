class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        hashmap = {}
        for i in range(len(nums1)):
            if hashmap.get(nums1[i]) is None:
                hashmap[nums1[i]] = 1
            else:
                hashmap[nums1[i]] += 1
        for i in range(len(nums2)):
            if hashmap.get(nums2[i]) is not None:
                if hashmap[nums2[i]] > 0:
                    intersect.append(nums2[i])
                    hashmap[nums2[i]] -= 1
        return intersect