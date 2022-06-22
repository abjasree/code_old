class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.bi_search(0,right=len(self.nums)-1)
        
        
    def bi_search(self, left, right):
        if left > right:
            return -1
        mid=(left+right)//2
        if  self.target == self.nums[mid]:
            return mid
        elif self.nums[mid] < self.target:
            return self.bi_search(mid+1,right)
        else:
            return self.bi_search(left,mid-1)
        
    
    def iterative_search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<= right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                 left=mid+1
            else:
                right=mid-1
        return -1