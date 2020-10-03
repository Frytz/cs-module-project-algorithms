'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    seen = [0] * len(arr)
    for i in range(len(arr)):
        seen[arr[i]] += 1
    
    index = 0
    while index < len(seen):
        if (seen[index] != 2 and seen[index] != 0):
            return index
        index += 1




    # pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")