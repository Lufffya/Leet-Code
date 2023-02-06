# https://leetcode.cn/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False        

        aphabets = {}
        for i in s:
            if i in aphabets:
                aphabets[i] += 1
            else:
                aphabets[i] = 1

        for i in t:
            if i in aphabets:
                aphabets[i] -= 1
            else:
                return False

        return all([i == 0 for i in aphabets.values()])


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("aacc", "ccac") == True
    assert s.isAnagram("rat", "car") == False