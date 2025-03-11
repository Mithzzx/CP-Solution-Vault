l = int(input())
for _ in range(l):
    n = input()
    n = n[::-1]
    c = 0

    for i in n:
        if i == "0":
            c += 1
        else:
            break

    n = n[::-1]
    n = n[:len(n) - c - 1]

    for i in n:
        if i != "0": c += 1

    print(c)
