def find_unique(x):
    unique_nums = []
    for i in x:
        if i not in unique_nums:
            unique_nums.append(i)
    return unique_nums




x = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print find_unique(12, 24, 35, 24, 88, 120, 155, 88, 120, 155)
