import sys
import random
from time import time

def insertionSort(arr):
    # Go through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1] to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def selectionSort(array):
    size = len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])


def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        l = arr[:mid]
        r = arr[mid:]
 
        # Sorting the first half
        mergeSort(l)
 
        # Sorting the second half
        mergeSort(r)
 
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = r[i]
            i += 1
            k += 1
 
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

def partition(array, leftmost, rightmost):
 
    # choose the rightmost element as pivot
    pivot = array[rightmost]
 
    # pointer for greater element
    i = leftmost - 1

    for j in range(leftmost, rightmost):
        if array[j] <= pivot:
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element
    (array[i + 1], array[rightmost]) = (array[rightmost], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

        
name = sys.argv[1]
arrSize = int(sys.argv[3])
numOfArr =int(sys.argv[2])

totalTime = 0
# Create array
for i in range(numOfArr):
    list= []
    for j in range(arrSize):
        list.append(random.uniform(0,10000))
    #Record start time
    time1= time()
    if name == "selectionSort":
        selectionSort(list)
    elif name == "insertionSort":
        insertionSort(list)
    elif name == "mergeSort":
        mergeSort(list)
    elif name == "quickSort":
        quickSort(list,0,arrSize-1)
    #Record end time
    time2= time()

    #Get the difference between start and end time in ms
    totalTime+=time2-time1
totalTime= totalTime * 10 ** 3

print("The average time of execution of above program is: ",totalTime/numOfArr , "ms")

