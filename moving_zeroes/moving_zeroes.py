'''
Input: a List of integers
Returns: a List of integers
'''

import time
from memory_profiler import profile

start = time.time()
@profile()
def moving_zeroes(arr):
    # Your code here 
    k = 0
    for i in arr:
        if i:
            arr[k] = i
            k = k + 1
    for i in range(k, len(arr)):
        arr[i] = 0
    return arr
    # a = [0 for i in range(arr.count(0))]
    # x = [i for i in arr if i != 0]
    
    # return x + a
end = time.time()

print(f" Runtime: {start - end:0.7f} seconds")


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")