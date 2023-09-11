class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if hashmap.get(nums[i]) is None:
                hashmap[nums[i]] = False
            elif hashmap[nums[i]] == False:
                hashmap[nums[i]] = True
        for key in hashmap.keys():
            if hashmap[key] == False:
                return key