class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        OpenToClose = {"{":"}","[":"]","(":")"}

        for c in s:
            if c in OpenToClose:
                stack.append(c)
            else:
                if stack and OpenToClose[stack[-1]] == c:
                    stack.pop()
                else: 
                    return False
        return not stack 
