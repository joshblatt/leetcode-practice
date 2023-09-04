class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if hashmap.get(nums[i]) is None:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
            if hashmap[nums[i]] > len(nums) / 2:
                return nums[i]
        return nums[i]