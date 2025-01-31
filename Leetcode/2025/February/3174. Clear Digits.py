s = "abc23"
stack = []

for i in s:
    if i.isnumeric():
        stack.pop(-1)
    else:
        stack.append(i)

print(stack)





