while True:
    line = input()
    if line == '.':
        break

    stack = []
    balanced = True

    for ch in line:
        if ch in '([':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()

    if balanced and not stack:
        print("yes")
    else:
        print("no")
