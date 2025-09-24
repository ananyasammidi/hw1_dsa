'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
def interval_covering(M: int, intervals: list) -> list:
    intervals = sorted(intervals, key=lambda x: x[1])
    result = []
    ending = float("-inf")

    for start, end in intervals:
        if start >= ending:
            result.append((start, end))
            ending = end

    return result
    
