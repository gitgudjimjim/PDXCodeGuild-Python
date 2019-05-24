# practice_dict_problems
def lists_to_dict(keys, values):
    """
    returns dictionary of keys mapped to values
    :keys: list
    :values: list
    """
    # combined = {}
    # for i in range(len(keys)):
    #     # print(i, keys[i], values[i])
    #     combined[keys[i]] = values[i]
    # return combined

    # # equivalent to above
    # return {keys[i]:values[i] for i in range(len(keys))}

    return dict(zip(keys, values))


fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
print(lists_to_dict(fruits, prices)) # -> {'apple':1.2, 'banana':3.3, 'pear':2.1}
