class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        min_loop = min(len(word1), len(word2))
        for i in range(min_loop):
            res += word1[i]
            res += word2[i]

        res += word1[i+1:] or word2[i+1:]

        return res
        