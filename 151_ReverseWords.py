# 151. Reverse Words in a String
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         x = s.split()
#         return " ".join(x[::-1])


class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        temp = ""
        for character in s:
            if character != " ":
                temp += character
            elif temp != "":
                res.append(temp)
                temp = ""
        if temp != "":
            res.append(temp)
        return " ".join(res[::-1])


s = "leetCODE is          difficult"
sol = Solution()
print(sol.reverseWords(s))
