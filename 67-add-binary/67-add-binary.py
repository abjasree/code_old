class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        carry = 0
        while a != '' or b != '':
            if a == '':
                cur_a = 0
                cur_b = int(b[-1])
                b = b[:-1]
            elif b == '':
                cur_b = 0
                cur_a = int(a[-1])
                a = a[:-1]
            else:
                cur_a = int(a[-1])
                cur_b = int(b[-1])
                a = a[:-1]
                b = b[:-1]
    
            if (cur_a + cur_b + carry) == 3 :
                carry = 1
                ans = '1' + ans
            elif (cur_a + cur_b + carry) == 2:
                carry = 1
                ans = '0' + ans
            elif  (cur_a + cur_b + carry) == 1:
                carry = 0
                ans = '1' + ans
            elif (cur_a + cur_b + carry) == 0:
                carry = 0
                ans = '0' + ans
                
        if carry != 0:
            ans = '1' + ans
                
        return ans
                
        