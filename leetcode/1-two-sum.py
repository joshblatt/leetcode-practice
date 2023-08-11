class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # space efficient solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # time efficient solution
        hashtable = {}
        for i in range(len(nums)):
            hashtable[nums[i]] = i
        for i in range(len(nums)):
            if hashtable.get(target - nums[i]):
                if hashtable[target - nums[i]] != i:
                    return [i, hashtable[target - nums[i]]]