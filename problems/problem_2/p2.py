'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
def interval_covering(M: int, intervals: list) -> list:
    intervals.sort(key=lambda x: (x[0], -x[1]))
    covering = []
    ending = float("-inf")

    for start, end in intervals:
        if end > ending:
            covering.append([start, end])
            ending = end

    return covering
    
