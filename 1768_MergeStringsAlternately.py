# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         result = []
#         minLength = min(len(word1), len(word2))
#
#         for i in range(minLength):
#             result.append(word1[i])
#             result.append(word2[i])
#
#         result.extend([word1[minLength:], word2[minLength:]])
#         return ''.join(result)
#
#
# word1 = "abc"
# word2 = "xyzpqr"
# sol = Solution()
# print(sol.mergeAlternately(word1, word2))

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        diff = min(len(word1), len(word2))
        resultString = ""
        for i in range(diff):
            resultString += word1[i] + word2[i]
        resultString += word1[diff:] + word2[diff:]
        return resultString


word1 = "abc"
word2 = "xyzqwer"
sol = Solution()
print(sol.mergeAlternately(word1, word2))
