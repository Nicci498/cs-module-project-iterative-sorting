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

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -=1
# STRETCH: implement the Count Sort function below
# requires us to know the max value
#
def count_sort(arr, maximum=-1):
    #if arr empty
    if len(arr) == 0:
        return arr
    # if max isnt given
    if maximum == -1:
        maximum = max(arr)
    # make a bunch of buckets (enough for each value 0 - max)
    buckets = [0 for i in range(maximum + 1)]

    for x in arr:
        if x < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[x] +=1

    # now we have the counts of every value in array
    # loop through our buckets starting at the smallest index
    j = 0
    for i in range(len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1

    return arr
