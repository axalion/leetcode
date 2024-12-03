class Solution:
    def isValid(self, s: str) -> bool:
        par_stack = []
        if not s:
            return True
        if s[0] in ["]", ")", "}"]:
            return False
        
        for char in s:
            if char in  ["[", "(", "{"]:
                par_stack.append(char)
            elif char == "]" and par_stack and par_stack[-1] == "[":
                par_stack.pop()
            elif char == ")" and par_stack and par_stack[-1] == "(":
                par_stack.pop()
            elif char == "}" and par_stack and par_stack[-1] == "{":
                par_stack.pop()
            else:
                return False
        return True if not par_stack else False
