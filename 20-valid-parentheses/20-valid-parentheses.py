class Solution:
    def isValid(self, s: str) -> bool:
        open_char = ['(', '{', '[']
        closed_char = [')', '}', ']']
        open_close = {}
        for i in range(len(open_char)):
            open_close[closed_char[i]] = open_char[i]
            
        stack = []
       
        for i in s:
            if i in open_char:
                stack.append(i)
            elif i in closed_char:
                if stack == []:
                    return False
                else:
                    if stack.pop() != open_close[i]:
                        return False
                    
        return stack == []
       
       
            
            