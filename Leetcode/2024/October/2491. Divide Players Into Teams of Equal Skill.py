skill = [3,2,5,1,3,4]

skill.sort()
x=0

lp,rp = 0,len(skill)-1
s=skill[0]+skill[-1]
while lp<rp:
    if s==skill[lp]+skill[rp]:
        x+= skill[lp]*skill[rp]
        lp+=1
        rp-=1
    
print(x)
