class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_dict = {}
        for i in s:
            if i in word_dict.keys():
                word_dict[i] = word_dict[i] + 1
            else:
                word_dict[i] = 1
                
        for j in t:
            if j not in word_dict.keys():
                return False
            else:
                word_dict[j] = word_dict[j] - 1
                
        return (not any(word_dict.values()))
    
        
        
    def brute_force_isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return s == t