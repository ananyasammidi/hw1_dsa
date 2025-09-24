import collections
'''
Problem 4c

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n).
'''
def most_frequent_difference_c(values, d_mode) -> int:
    count = collections.Counter(values)
    frequency = 0

    for i in values:
        frequency += count.get(i + d_mode, 0)
        if d_mode == 0:
            frequency -= 1

    return frequency
