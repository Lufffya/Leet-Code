# https://leetcode.cn/problems/zigzag-conversion/


### 初步设想 ###
# 思路: 事先创建好 numRows 行的数组, 遍历字符串, 将字符放入对应的行 
# e.g: numRows = 3, 于是 i = > 0, 1, 2, 1, 0, 1, 2, 1 ,0, 1 ,2 .......
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        i, move = -1, 1
        rows = [[] for _ in range(numRows)]
        for _s in s:
            
            if move == 1 and i != numRows:
                i += 1
            elif move == -1 and i != 0:
                i -= 1
                
            if i+1 == numRows:
                move = -1
            elif i == 0:
                move = 1
                
            rows[i].append(_s)
           
        return ''.join(sum(rows, []))
### 结果 ### 
# 执行用时: 68 ms, 在所有 Python3 提交中击败了 40.80% 的用户
# 内存消耗: 15.1 MB, 在所有 Python3 提交中击败了 63.70% 的用户


### 大神贴图 ###
# 思路: 
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res, n = [''] * numRows, 2 * numRows - 2

        for i, c in enumerate(s):
            res[min(idx := i % n, n - idx)] += c
        
        return ''.join(res)


if __name__ == "__main__":
    # P A Y P A L I S H I R I N G
    # P A H N A P L S I I G Y I R
    
    # P   A   H   N
    # A P L S I I G
    # Y   I   R
    
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))
