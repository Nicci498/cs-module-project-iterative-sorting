# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # * track the current index
    current = 0
    # * while current index is less than the length of the array - 1
    while current < len(arr) - 1:
        smallest = current
        # loop through the (sub)array
        for i in range(current + 1, len(arr)):
            # * if smallest is greater than i, smallest now equals i
            if arr[smallest] > arr[i]:
                smallest = i
        # ! the loop has finished, smallest now represents the lowest value from current until the end of the array
        # swap the values of current with smallest
        arr[current], arr[smallest] = arr[smallest], arr[current]
        # we have completed all steps for that index, now do it again until we reach the end of the array
        current += 1
    # we have reached the end of the array, return array
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    #run through array
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            # compare which is greater, if next val is greater
            if arr[j] > arr[j + 1]:
                # switch
                # temp = arr[j]
                # arr[j] = arr[j + 1]
                # arr[j+1] = temp
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
