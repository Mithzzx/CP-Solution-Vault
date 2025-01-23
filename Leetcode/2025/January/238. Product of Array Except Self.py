nums = [1,2,3,4]
#Output: [24,12,8,6]
x=[1]*len(nums)

l=1
for i in range(len(nums)-1):
    l = l*nums[i]
    x[i+1] = l
    print(l,x)
r=1
for i in range(1,len(nums)):
    r = r*nums[-i]
    x[-i-1] *= r
    print(r,x)
