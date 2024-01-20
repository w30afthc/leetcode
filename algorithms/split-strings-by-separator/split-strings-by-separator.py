"""
title : 2788. Split Strings by Separator
source : https://leetcode.cn/problems/split-strings-by-separator/
"""
from typing import List


class Solution:
    """暴力拆分

    遍历每个字符串，如果当前字符不是分隔符则累加到新字符串中
    如果当前字符是新分隔符，则之前把之前累加的非空字符串追加到结果列表中
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            new_word = ""
            for i in range(len(word)):
                if word[i] == separator:
                    if new_word:
                        result.append(new_word)
                    new_word = ""
                else:
                    new_word += word[i]
            if new_word:
                result.append(new_word)
        return result


if __name__ == "__main__":
    print(Solution().splitWordsBySeparator(words=["one.two.three","four.five","six"], separator="."))
    print(Solution().splitWordsBySeparator(words=["$easy$","$problem$"], separator="$"))
    print(Solution().splitWordsBySeparator(words=["|||"], separator="|"))
