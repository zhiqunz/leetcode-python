"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ""
        length = 0
        for i in s:
            if i not in tmp:
                tmp += i
            else:
                if len(tmp) > length:
                    length = len(tmp)
                tmp = tmp[tmp.index(i) + 1:] + i
        if len(tmp) > length:
            length = len(tmp)

        return length

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 如果参数不是字符串，返回0
        if type(s) != str or not s:
            return 0
        if len(s) == 1:
            return 1

        length = 0
        loop_count_max = 10000
        loop_count = 0
        # 循环条件 最长子串已经大于等于剩余字符串，或者 字符串全部处理完毕 或者 循环超高10000次
        while length < len(s) and loop_count_max > loop_count:
            # 获取最大子字符串
            for i in range(0, len(s)):
                if s.index(s[i]) < i and i:
                    if i > length:
                        length = i
                    break
                elif i + 1 == len(s):
                    if i + 1 > length:
                        length = i + 1
                    break
            # 从下一个字符开始继续循环寻找
            s = s[1:]
            loop_count += 1

        return length


if __name__ == '__main__':
    s1 = Solution()
    str1 = 'a'
    str2 = 'ab'
    str3 = 'abcabcbb'
    print(s1.lengthOfLongestSubstring(str1))
    print(s1.lengthOfLongestSubstring(str2))
    print(s1.lengthOfLongestSubstring(str3))
