# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left
                
        
            
        
        
    def brute_force_firstBadVersion(self, n: int) -> int:
        for i in range(1, n+1):
            if isBadVersion(i) == True:
                return i
        