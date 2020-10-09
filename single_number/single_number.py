import time

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
start_time=time.time()
def single_number(arr):
    
    ans = arr[0]
    for i in range(1,len(arr)):
        ans ^= arr[i] #XOR bitwise operation O(1) = constant time    
    return ans
end_time=time.time()
    
print(f"runtime: {end_time - start_time:0.6f} seconds")
    



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
