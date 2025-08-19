vowels = {'a', 'e', 'i', 'o', 'u','y','A', 'E', 'I', 'O', 'U','Y'}

x = input()
y = ""
for i in x:
    if i in vowels:
        continue
    elif 'A' <= i <= 'Z':
        y += "."+chr(ord(i) + 32)
    else:
        y += "."+i

print(y)
