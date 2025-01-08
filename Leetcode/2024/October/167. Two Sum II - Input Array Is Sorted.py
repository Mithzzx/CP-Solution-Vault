numbers = [2,7,11,15]
target = 9
lp = 0
rp = len(numbers)-1
while lp>rp:
    sum = numbers[lp]+numbers[rp]
    if sum == target:
        print(lp,rp)
    elif sum > target:
        rp-=1
    else:
        lp+=1