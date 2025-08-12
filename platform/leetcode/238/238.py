from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res


if __name__ == "__main__":
    print(productExceptSelf([1, 2, 3, 4]))
