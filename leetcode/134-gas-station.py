class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gain = 0
        total_gain = 0
        index = 0
        for i in range(len(gas)):
            cur_gain += gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            if cur_gain < 0:
                index = i + 1
                cur_gain = 0
        return index if total_gain >= 0 else -1