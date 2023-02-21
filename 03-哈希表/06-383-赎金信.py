# https://leetcode.cn/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        val_dict = {}
        for s in magazine:
            if s in ransomNote:
                if s in val_dict:
                    val_dict[s] += 1
                else:
                    val_dict[s] = 1

        for s in ransomNote: 
            if s not in val_dict or val_dict[s] == 0:
                return False
            else: 
                val_dict[s] -= 1

        return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "ab"
    print(Solution().canConstruct(ransomNote, magazine))