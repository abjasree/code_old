class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if i == "+":
                    stack.append(num1+num2)
                elif i == "-":
                    stack.append(num1-num2)
                elif i == "*":
                    stack.append(num1*num2)
                else:
                    stack.append(int(num1/num2))
        return stack.pop()
            
        