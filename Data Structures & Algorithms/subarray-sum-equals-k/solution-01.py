nums = [-4, 5, 6 ,1]
k = 4

result = []
for i in range(len(nums)):
    csum = 0
    
    for j in range(i, len(nums)):
        csum += nums[j]
        
        if csum % k == 0:
            print(i, j, nums[i:j+1])
            result.append(nums[i:j+1])
        
print(result)

# output -> [[-4], [-4, 5, 6, 1], [5, 6, 1]]
