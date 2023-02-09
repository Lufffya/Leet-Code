# https://leetcode.cn/problems/reconstruct-itinerary/

# from typing import List


# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:

#             def backtrack(_from, tickets_dict):
                
#                 _tickets = tickets_dict[_from]

#                 if len(_tickets) == 0:
#                     res.append(path[:])
                
#                 for _ in tickets_dict[_from]:
#                     tickets_dict[start_point].pop(0)
                    
#                     path.append(to)
#                     backtrack(to)
#                     path.pop()

#             from collections import defaultdict

#             tickets_dict = defaultdict(list)
#             for item in tickets:
#                 tickets_dict[item[0]].append(item[1])

#             path = ['JFK']
#             res = []
#             backtrack('JFK', tickets_dict[:])
#             return res[0]


# if __name__ == "__main__":
#     tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#     print(Solution().findItinerary(tickets))


