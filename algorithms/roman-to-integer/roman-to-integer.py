"""
source : https://leetcode.cn/problems/roman-to-integer/description/
"""
from typing import List


class Solution:
    """
    小值在大值左边则相减，小值在大值右边则相加
    """
    def romanToInt(self, s: str) -> int:
        transfer_dict ={
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        i, result = 0, 0
        while i < len(s):
            if i < len(s) - 1 and transfer_dict[s[i]] < transfer_dict[s[i+1]]:
                result -= transfer_dict[s[i]]
            else:
                result += transfer_dict[s[i]]
            i += 1

        return result


class Solution1:
    """
    直接将可能得转换都列出来，从左到右先判断 2 个字符，符合则相加
    不符合则判断 1 个字符
    """
    def romanToInt(self, s: str) -> int:
        transfer_dict ={
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        integer = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in transfer_dict:
                integer += transfer_dict[s[i:i+2]]
                i += 2
            elif s[i] in transfer_dict:
                integer += transfer_dict[s[i]]
                i += 1

        return integer


if __name__ == "__main__":
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("IV"))
    print(Solution().romanToInt("IX"))
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))

