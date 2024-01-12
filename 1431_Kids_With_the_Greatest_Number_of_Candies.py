class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n = len(candies)
        maximum = max(candies)
        answerList = []
        for i in range(n):
            sumValue = candies[i] + extraCandies
            if sumValue >= maximum:
                answerList.append(True)
            else:
                answerList.append(False)

        return answerList


candies = [4,2,1,1,2]
extraCandies = 2
sol = Solution()
print(sol.kidsWithCandies(candies, extraCandies))
