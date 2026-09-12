class Solution:
    def isValid(self, s: str) -> bool:
        a = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                a.append(ch)

            else:
                if len(a) == 0:
                    return False

                x = a.pop()

                if ch == ')' and x != '(':
                    return False
                if ch == ']' and x != '[':
                    return False
                if ch == '}' and x != '{':
                    return False

        return len(a) == 0