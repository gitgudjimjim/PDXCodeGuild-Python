"""
Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
"""
def find_pair(nums, target):
    nums = []
    target = int(input("enter the target number:"))
    for i in range(len(nums)):
        if i < target:
            difference = int(target) - int(i)
            if difference in nums:
                print("success!('i', 'difference')")
                break
print(find_pair)([5, 6, 2, 3], 7)
print(find_pair)([5, 2, 6, 3], 7)
