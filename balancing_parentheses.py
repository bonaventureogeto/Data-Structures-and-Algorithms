def is_balanced(s):
    stack = []
    matching_par = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != matching_par[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced(""))
