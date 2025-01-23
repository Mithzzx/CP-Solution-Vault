height = [0,1,0,2,1,0,1,3,2,1,2,1]
lp,rp = 0,1
while lp<len(height)-1:
    mh = 0
    i=0
    if height[rp] >= height[lp]:
        print(lp, rp)
        lp = rp
        rp+=1
    elif rp<len(height)-1:
        if height[rp] > mh:
            mh = height[rp]
            i = rp
        rp+=1
    else:
        lp = i
        rp = i+1
        mp = 0
        i=0