def makeGood(s: str) -> str:
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        elif (c.lower() == stack[-1] or c.upper() == stack[-1]) and c != stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

print(makeGood("leEeetcode"))
print(makeGood("abBAcC"))
print(makeGood("s"))
