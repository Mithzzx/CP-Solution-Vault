for j in [[1,1,1],[6,10,6],[7,9,1,1,1,3],[2,1,3,4],[3,6,10,1,8,9,9,8,9]
]:
    nums = j
    minindex = 0
    maxindex = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[minindex]:
            minindex = i
        if nums[i] > nums[maxindex]:
            maxindex = i
    print(minindex, maxindex)
    dif = abs(minindex - maxindex)
    print(dif <= 1 or dif == len(nums) - 1)

