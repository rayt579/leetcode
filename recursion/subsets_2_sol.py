def subsets_without_recursion(nums):
    subsets = [[]]
    nums.sort()
    i = 0
    while i < len(nums):
        count = 0
        while i + count < len(nums) and nums[i + count] == nums[i]:
            count += 1
        
        previous_length = len(subsets)
        for j in range(previous_length):
            instance = subsets[j]
            print(instance)
            for k in range(count):
                instance.append(nums[i])
                subsets.append(list(instance))
        i += count
    return subsets
