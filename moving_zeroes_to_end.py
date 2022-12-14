"""

Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]
"""

def move_zeros(array):
    zero_count = 0
    while 0 in array:
        array.remove(0)
        zero_count += 1
    i = 0
    while i < zero_count:
        array.append(0)
        i += 1
    return array