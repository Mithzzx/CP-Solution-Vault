matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

n = len(matrix)
c=[]
for i in range(0,n):
    c.append([])
    for j in range(0,n):
        c[-1].append(0)
for i in range(0,n):
    for j in range(0,n):
        c[-1].append(0)
        c[j][-(i+1)]=matrix[i][j]
print(c)