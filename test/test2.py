class Solution:
    def evalRPN(self, tokens) -> int:
        stack=[]
        while tokens:
            ele = tokens.pop(0)
            if ele in '+-*/':
                # 出栈两个，算完入栈
                n2 = stack.pop()
                n1 = stack.pop()
                n3 = int(eval(n1+ele+n2))
                stack.append(str(n3))
            else:
                stack.append(ele)
        print(int(stack[0]))
        return stack[0]



s=Solution()
s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])