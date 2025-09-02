class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # invariant: if target is in nums, then it must be between l and r. 
        ## That is, l <= idx <= r where nums[idx]=target if target in nums
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            if nums[mid] <= nums[r]:
                if nums[r] == target:
                    return r
                if nums[mid] < target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] == target:
                    return l
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
