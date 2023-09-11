class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if hashmap.get(nums[i]) is None:
                hashmap[nums[i]] = True
            elif hashmap[nums[i]]:
                return True
        return False