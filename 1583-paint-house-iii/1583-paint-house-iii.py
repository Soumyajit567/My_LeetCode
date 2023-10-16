from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        MAX_COST = 10**7
        
        # Renaming the memoization structure to 'dp'.
        dp = {}
        
        # Renaming the function to 'memo'.
        @cache
        def memo(house, target, last_color):
            if target < 0:  # Too many neighborhoods
                return MAX_COST
            if house == m:  # All houses considered
                return 0 if target == 0 else MAX_COST

            # Check if the result is already computed and stored in 'dp'.
            if (house, target, last_color) in dp:
                return dp[(house, target, last_color)]

            min_cost = MAX_COST
            if houses[house]:  # If the house is already painted
                new_neighborhood = last_color != houses[house]
                adjusted_target = target - (1 if new_neighborhood else 0)
                cost_if_same = memo(house + 1, adjusted_target, houses[house])
                min_cost = min(min_cost, cost_if_same)
            else:
                for color in range(1, n + 1):
                    new_color= last_color != color
                    adjusted_color = target - (1 if new_color else 0)
                    cost_to_paint = cost[house][color - 1] + memo(house + 1, adjusted_color, color)
                    min_cost = min(min_cost, cost_to_paint)

            # Store the result in 'dp' for future reference.
            dp[(house, target, last_color)] = min_cost
            return min_cost

        # We start from the first house, with 'target' neighborhoods, and '0' as the last color (since no house is painted yet).
        result = memo(0, target, 0)
        return -1 if result >= MAX_COST else result




















"""
from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        MAX_COST = 1000001
        memo = [[[MAX_COST] * n for _ in range(target + 1)] for _ in range(m)]

        for color in range(1, n + 1):
            if houses[0] == color:
                memo[0][1][color - 1] = 0
            elif not houses[0]:
                memo[0][1][color - 1] = cost[0][color - 1]

        for house in range(1, m):
            for neighborhoods in range(1, min(target, house + 1) + 1):
                for color in range(1, n + 1):
                    if houses[house] and color != houses[house]:
                        continue

                    currCost = MAX_COST
                    for prevColor in range(1, n + 1):
                        if prevColor != color:
                            currCost = min(currCost, memo[house - 1][neighborhoods - 1][prevColor - 1])
                        else:
                            currCost = min(currCost, memo[house - 1][neighborhoods][color - 1])

                    costToPaint = 0 if houses[house] else cost[house][color - 1]
                    memo[house][neighborhoods][color - 1] = currCost + costToPaint

        minCost = min(memo[m - 1][target])
        return -1 if minCost >= MAX_COST else minCost
"""


        