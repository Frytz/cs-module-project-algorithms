'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, arr=None):
    # base case
    if n < 0:
        return 0
    # this represents there being a number of cookies where we can
    # just take that many cookies
    elif n == 0:
        return 1
    # check the arr to see if the answer is stored there
    elif arr and arr[n] > 0:
        return arr[n]
    else: 
        if not arr:
            # init an empty arr
            arr = {i: 0 for i in range(n+1)}
        # store answers in our arr
        arr[n] = eating_cookies(n - 1, arr) + eating_cookies(n - 2, arr) + eating_cookies(n - 3, arr)
    return arr[n]
    # pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
