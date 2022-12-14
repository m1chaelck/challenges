"""
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals,
and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. 
The first value of the interval will always be less than the second value. 
Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.
"""

def sum_of_intervals(intervals):
    number = []
    maxn = 0
    minn = 0
    for i in intervals:
        if i[1] > maxn:
            maxn = i[1]
        if i[0] < minn:
            minn = i[0]
    for i in range(0, maxn - minn):
        number.append(0)
    for i in intervals:
        for j in range(i[0]-minn, i[1]-minn):
            number[j] = 1   
    return sum(number)