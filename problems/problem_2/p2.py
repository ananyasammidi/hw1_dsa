'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
def interval_covering(M: int, intervals: list) -> list:
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    result = []
    i = 0
    n = len(intervals)
    current_end = 0

    while current_end < M:
        best_end = current_end
        best_interval = None
        
        while i < n and intervals[i][0] <= current_end:
            if intervals[i][1] > best_end:
                best_end = intervals[i][1]
                best_interval = intervals[i]
            i += 1

        if best_interval is None:
            return []

        result.append(best_interval)
        current_end = best_end

    return result