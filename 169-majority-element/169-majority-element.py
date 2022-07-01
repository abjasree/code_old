class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict={}
        n = len(nums)
        for i in nums:
            if i not in num_dict.keys():
                num_dict[i] = 1
            num_dict[i] += 1
            if num_dict[i] > n//2 + 1:
                return i
                