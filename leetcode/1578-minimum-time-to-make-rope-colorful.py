class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        for i in range(len(colors) - 1):
            if colors[i] == colors[i + 1]:
                time += min(neededTime[i], neededTime[i+1])
                if neededTime[i] > neededTime[i+1]:
                    # swap to carry forward the bigger number
                    temp = neededTime[i]
                    neededTime[i] = neededTime[i+1]
                    neededTime[i+1] = temp
        return time