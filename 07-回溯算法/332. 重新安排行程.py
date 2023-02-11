# https://leetcode.cn/problems/reconstruct-itinerary/

from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_dict = defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])

        for airport in tickets_dict: tickets_dict[airport].sort()

        path = ["JFK"]
        def backtracking(start_point):

            if len(path) == len(tickets) + 1:
                return True
            for _ in tickets_dict[start_point]:
                #必须及时删除，避免出现死循环
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)
                if backtracking(end_point):
                    return True
                path.pop()
                tickets_dict[start_point].append(end_point)

        backtracking("JFK")
        return path

if __name__ == "__main__":
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(Solution().findItinerary(tickets))