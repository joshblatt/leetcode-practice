# O(n) time O(n) space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if hashmap.get(nums[i]) is None:
                hashmap[nums[i]] = i
            elif abs(hashmap[nums[i]] - i) > k:
                hashmap[nums[i]] = i
            elif abs(hashmap[nums[i]] - i) <= k:
                return True
        return False