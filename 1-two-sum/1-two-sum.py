class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in num_dict.keys():
                return [num_dict[target-nums[i]], i]
            else:
                num_dict[nums[i]] = i 
        
                
        
    def brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] ==  target:
                    return [i,j]
                