'''
Problem 4a

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n^2).
'''
def most_frequent_difference_a(values, d_mode) -> int:
    frequency = 0
    for i in range(len(values)):
        for j in range(len(values)):
            if i != j and values[i] - values[j] == d_mode:
                frequency = frequency + 1
    return frequency
