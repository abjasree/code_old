class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = [i for i in s if i.isalnum()]
        reverse = s_new[::-1]
       
        return s_new == reverse
        