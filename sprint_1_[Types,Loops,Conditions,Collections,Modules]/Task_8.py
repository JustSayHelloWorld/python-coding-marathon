"""'s3ooOOooDy' has exams. He wants to study hard this time. He has an array of studying hours per day for the previous exams. He wants to know the length of the maximum non-decreasing contiguous subarray of the studying days, to study as much before his current exams.

Example:

For a = [2,2,1,3,4,1] the answer is 3.

[input] array.integer a

The number of hours he studied each day.

[output] integer

The length of the maximum non-decreasing contiguous subarray.
"""


def studying_hours(a):
    day_counter = 0
    studying_hours = a[0]
    subbarray_length = []
    for element in a:
        if element >= studying_hours:
            studying_hours = element
            day_counter+=1
        else:
            subbarray_length.append(day_counter)
            day_counter = 1
            studying_hours = element
    subbarray_length.append(day_counter)

    return max(subbarray_length)