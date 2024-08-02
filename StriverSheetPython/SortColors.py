nums= [2, 0, 2, 1, 1, 0]

l, m, h = 0, 0, len(nums)-1

while m<=h:
    num = nums[m]
    if num == 0:
        nums[l],nums[m]=nums[m],nums[l]
        l+=1;m+=1
    elif num == 1:
        m+=1
    else:
        nums[m],nums[h]=nums[h],nums[m]
        h-=1
        
print(nums)