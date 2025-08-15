from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    def twosum_sorted(target, i, j):
        while i < j:
            sum_ = nums[i] + nums[j]
            if sum_ == target:
                return [i, j]
            elif sum_ < target:
                i += 1
            else:
                j -= 1
        return None

    nums.sort()
    n = len(nums)
    seen = []

    for i in range(n):
        if (
            i > 0 and nums[i] == nums[i - 1]
        ):  # add this to prevent duplicates in seen from first entry of subarrays
            continue
        # Optional early stop: once nums[i] > 0, no three numbers can sum to 0
        if nums[i] > 0:
            break

        l, r = i + 1, n - 1
        while l < r:
            match twosum_sorted(-nums[i], l, r):
                case None:
                    break
                case (a, b):
                    seen.append([nums[i], nums[a], nums[b]])
                    l, r = a + 1, b - 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
    return seen
