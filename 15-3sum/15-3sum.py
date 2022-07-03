class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s<0:
                    l += 1
                elif s>0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                                   l += 1
                    while l < r and nums[r] == nums[r-1]:
                                   r -= 1
                    l += 1
                    r -= 1
        return result
        
    def brute_force_threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        nums_list.append([nums[i], nums[j], nums[k]])
        res_list = []
        for i in range(len(nums_list)):
            sort_ls = sorted(nums_list[i])
            if sort_ls not in res_list:
                res_list.append(sort_ls)
        return res_list
                
        