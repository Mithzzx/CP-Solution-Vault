s = "())"
#Output: 1
stack = []

for i in s:
    if i == '(':
        stack.append(i)
    else:
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)

print(len(stack))
