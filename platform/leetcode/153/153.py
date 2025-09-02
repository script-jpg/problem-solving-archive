class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        assert n != 0, "minimum DNE"
        # invariant: nums[idx] is always <= nums[n-1]
        idx = n-1
        l, r = 0, n-1 # establish l and r pointers
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= nums[n-1]: 
                idx = mid # nums[idx] <= nums[n-1] since idx=mid
                r = mid - 1 # if rotated, then r = mid - 1 guarantees smaller solution if it can be found
            else:
                l = mid + 1
        # Termination: we've moved up l as far up as we can. We've moved r down whenever we've found a working solution. We've set idx=mid when a new solution arises. idx must now be the index of the min. Invariant is maintained throughout.
        return nums[idx]
