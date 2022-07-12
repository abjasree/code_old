class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p_1 = 0
        p_2 = 0 
        substring = set()
        maxim = 0
        while p_2 < len(s):
            if s[p_2] not in substring:
                substring.add(s[p_2])
                p_2 += 1
            else:
                if len(substring) > maxim:
                    maxim = len(substring)
                substring.remove(s[p_1])
                p_1 += 1
        if len(substring) > maxim:
            maxim = len(substring)
        return maxim    
            
            
        def brute_force_lengthOfLongestSubstring(self, s: str) -> int:
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
                