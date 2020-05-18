def linear_search(arr, target):
    # Your code here
    for num in range(len(arr)):
        if arr[num] == target:
            return num        
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #determine size of arr
    left = 0
    right = len(arr) - 1
    #find mid
    while left <= right:
        mid = (left + right)//2
        #if mid is equal to target
        if arr[mid] == target:
            return mid

        # Check if we go left or right
        if arr[mid] < target:
            # if target is greater toss out right
            left = mid + 1
        else:
            # if target is greater toss out right
            right = mid - 1

    return -1  # not found
