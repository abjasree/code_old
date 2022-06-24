class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if sums + nums[i]> nums[i]:
                sums = sums + nums[i]
            else:
                sums = nums[i]
            if sums > max_sum:
                max_sum = sums
            
        return max_sum
            
                
    def brute_force_maxSubArray(self, nums: List[int]) -> int:
        sum_list = []
        
        for i in range(len(nums)+1):
            for j in range(i+1, len(nums)+1):
                temp = nums[i:j]
                sums = sum(temp)
                sum_list.append(sums)
            
        return max(sum_list)
                      
        