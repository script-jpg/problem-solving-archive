from typing import List

# naive implementation
def permute(nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(nums, curr):
            if len(curr) == n:
                res.append(curr[:])
            else:
                for i in range(len(nums)):
                    curr.append(nums[i])
                    helper(nums[:i]+nums[i+1:], curr)
                    curr.pop()
        helper(nums, curr=[])
        return res

# swapping implementation (no copying arrays)
def permute2(nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(first: int = 0):
            if first == n:
                res.append(nums[:])
            else:
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    helper(first + 1)
                    nums[first], nums[i] = nums[i], nums[first]
        helper()
        return res

if __name__ == '__main__':
    print("Using naive permute: ", permute([1,2,3]))
    print("Using swapping permute: ", permute2([1,2,3]))
