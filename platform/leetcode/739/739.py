class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s, res = [], [0]*len(temperatures)
        for i, num in enumerate(temperatures):
            while len(s) > 0 and num > temperatures[s[-1]]:
                top = s.pop()
                res[top] = (i - top)
            s.append(i)
        return res

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         s, res = [], [0]*len(temperatures)
#         for i, num in enumerate(temperatures):
#             while len(s) > 0 and num > s[-1][0]:
#                 top = s.pop()
#                 res[top[1]] = (i - top[1])
#             s.append((num, i))
#         return res
