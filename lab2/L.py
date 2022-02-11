n = input()
 
 
def OpenClosed(n):
    stack = []
    brackets = ["(", "{", "["]
    for char in n:
        if char in brackets:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack != []:
        return False
    return True

if OpenClosed(n):
    print("Yes")
else:
    print("No")