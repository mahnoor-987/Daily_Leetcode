class solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                top = stack.pop()

                if char == ')' and top!= '(':
                    return False
                if char == '}' and top!= '{':
                    return False
                if char == ']' and top!= '[':
                    return False
        return not stack
