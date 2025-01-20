s = "]]][[["
#Output: 1
stack = []

for i in s:
    if i == '[':
        stack.append('[')
    else:
        if stack and stack[-1] == '[':
            stack.pop()
        else:
            stack.append('[')

if len(stack)%2 == 0:
    print(len(stack)//2)
else:
    print (-1)
