class Solution:
    def findMin(self, nums: List[int]) -> int:
        assert(len(nums) != 0, "minimum DNE")
        # invariant: nums[idx] is always <= nums[0]
        idx = 0
        l, r = 0, len(nums)-1 # establish l and r pointers
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= nums[0]: 
                idx = mid # nums[idx] <= nums[0] since idx=mid
                r = mid - 1 # if rotated, then r = mid - 1 guarantees smaller solution if it can be found
            else:
                l = mid + 1
        # Termination: we've moved up l as far up as we can. We've moved r down whenever we've found a working solution. We've set idx=mid when a new solution arises. idx must now be the index of the min. Invariant is maintained throughout.
        return nums[idx]

