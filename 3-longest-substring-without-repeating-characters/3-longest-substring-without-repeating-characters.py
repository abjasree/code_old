class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        
        long_len = []
        substring = {}
        for i in range(len(s)):
            substring[s[i]] = 0
            for j in range(i+1, len(s)):
                if s[j] not in substring.keys():
                    substring[s[j]] = 0
                else:
                    break
            long_len.append(len(substring))
            
            substring = {}
        
        return max(long_len)
            
            
        