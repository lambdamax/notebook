class Solution:
    def isValid(self, s: str) -> bool:
        ans = {')': '(', ']': '[', '}': '{'}
        s = list(s)
        stack = []
        while s:
            ele = s.pop(0)
            if stack and stack[-1] == ans.get(ele):
                stack.pop()
            else:
                stack.append(ele)
        if stack:
            print(False)
            return False
        print(True)
        return True

w = "([)]"
s=Solution()
s.isValid(w)
