import collections
import bisect
'''
Problem 4b

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n log n).
'''
def most_frequent_difference_b(values, d_mode) -> int:
    values.sort()
    frequency = 0

    if d_mode == 0:
        counts = collections.Counter(values)
        for j in counts.values():
            frequency += j * (j - 1)
        return frequency

    for i in values:
        target = i + d_mode
        left = bisect.bisect_left(values, target)
        right = bisect.bisect_right(values, target)
        frequency += (right - left)

    return frequency
        
