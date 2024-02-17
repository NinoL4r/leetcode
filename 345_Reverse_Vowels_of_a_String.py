# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         left = 0
#         right = len(s) - 1
#         vowels = "aeiouAEIOU"
#         s_list = list(s)
#
#         while left < right:
#             if s_list[left] not in vowels:
#                 left += 1
#             if s_list[right] not in vowels:
#                 right -= 1
#             if s_list[right] in vowels and s_list[left] in vowels:
#                 s_list[left], s_list[right] = s_list[right], s_list[left]
#                 right -= 1
#                 left += 1
#
#         return ''.join(s_list)



class Solution:
    def reverseVowels(self, s: str) -> str:
        left_pointer = 0
        right_pointer = len(s) - 1
        vowels = "aeiouAEIOU"
        s_list = list(s)

        while left_pointer < right_pointer:
            if s_list[left_pointer] not in vowels:
                left_pointer += 1
            if s_list[right_pointer] not in vowels:
                right_pointer -= 1
            if s_list[right_pointer] in vowels and s_list[left_pointer] in vowels:
                s_list[left_pointer], s_list[right_pointer] = s_list[right_pointer], s_list[left_pointer]
                right_pointer -= 1
                left_pointer += 1
        return ''.join(s_list)


str = "leetCODE"
sol = Solution()
print(sol.reverseVowels(str))
