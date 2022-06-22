class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_dict = [0 for i in range(26)]
        for i in s:
            word_dict[ord(i) - ord('a')] = word_dict[ord(i) - ord('a')] + 1
           
                
        for j in t:
            word_dict[ord(j) - ord('a')] = word_dict[ord(j) - ord('a')] - 1
        print(word_dict)   
        print(not any(word_dict))
        return not any(word_dict)
    
        
        
    def brute_force_isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return s == t