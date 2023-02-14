# https://leetcode.cn/problems/gas-station/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        start = 0
        total_gas = 0
        for i in range(len(gas)):

            total_gas += gas[i] - cost[i]

            if total_gas < 0:
                start = i + 1
                total_gas = 0
        
        return start


if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(Solution().canCompleteCircuit(gas, cost))