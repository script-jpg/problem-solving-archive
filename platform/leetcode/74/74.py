class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = m-1
        feasible = lambda x : x < m and matrix[x][-1] >= target
        l, r = 0, m-1
        while l <= r :
            mid = (l+r)//2
            if feasible(mid):
                row = mid
                r = mid - 1
            else:
                l = mid + 1
        # if not (0 <= row): return False
        l, r = 0, n-1
        arr = matrix[row]
        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target :
                return True
            elif arr[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return False        
