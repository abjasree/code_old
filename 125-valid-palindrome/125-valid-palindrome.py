class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = [i for i in s if i.isalnum()]
        left = 0
        right = len(s_new)-1
        while left < right:
            
            if s_new[left] == s_new[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
            
          
    
    def using_list_python_isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = [i for i in s if i.isalnum()]
        reverse = s_new[::-1]
       
        return s_new == reverse