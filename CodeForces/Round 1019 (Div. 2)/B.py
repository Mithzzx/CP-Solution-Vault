s = "000"
change,current = 0,s[0]
for i in s:
        if i != current:
            change += 1
            current = i
moves = 0 if s[0] == 0 else 1
current = s[0]
for i in s[1:]:
        if i != current:
            moves += 2
            current = i
        else:
            moves += 1
moves = moves-1 if change > 1 else moves
print(moves)



