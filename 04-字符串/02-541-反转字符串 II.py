# https://leetcode.cn/problems/reverse-string-ii/


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for i in range(0, len(s), 2*k):
            # if len(s[i:i+(2*k)]) != 2*k:
            #     continue
            s = s[:i] + s[i:i+(2*k)][:k][::-1] + s[i:i+(2*k)][k:] + s[i+(2*k):]

        # # 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样
        # if len(s) % (2*k) < (2 * k) and len(s) % (2*k) >= k:
        #     s = s[:len(s)//(2*k)*(2*k)] + s[len(s)//(2*k)*(2*k):len(s)//(2*k)*(2*k)+k][::-1] + s[len(s)//(2*k)*(2*k)+k:]

        # # 如果剩余字符少于 k 个，则将剩余字符全部反转。
        # elif (len(s) % (2*k)) < k:
        #     s = s[:len(s)//(2*k)*(2*k)] + s[len(s)//(2*k)*(2*k):][::-1]

        return s


if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    print(Solution().reverseStr(s, k))