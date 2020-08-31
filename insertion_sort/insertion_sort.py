from typing import List
import random

def insertion_sort(t):
    copy_t = t
    indexes = range(len(t))
    for i in range(len(t)):
        if i != 0:
            current = i
            while t[current] < t[current - 1] and current - 1 >= 0:
                t[current], t[current -1] = t[current - 1], t[current]
                current -= 1
    return t


if __name__ == '__main__':
    large_list = list(range(10))
    large_list_copy = large_list.copy()
    random.shuffle(large_list_copy)
    print(large_list_copy)
    print(insertion_sort(large_list_copy))
















































# Function to do insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
    return arr
