class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = [i for i in s if i.isalnum()]
       
        while len(s_new) > 0:
            if len(s_new) == 1:
                return True
            elif s_new[0] == s_new[-1]:
                s_new = s_new[1:-1]
            else:
                return False
        return True
            
          
    
    def test_isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = [i for i in s if i.isalnum()]
        reverse = s_new[::-1]
       
        return s_new == reverse