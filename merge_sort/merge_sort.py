from typing import List
import random


def merge_sort(list_to_sort: List[int]) -> List[int]:
    if len(list_to_sort) <= 1:
        return list_to_sort
    elif len(list_to_sort) == 2:
        if list_to_sort[0] > list_to_sort[1]:
            return list_to_sort[::-1]
        else:
            return list_to_sort
    else:
        split_index = len(list_to_sort) // 2
        return merge_lists(
            merge_sort(
                list_to_sort[:split_index],
            ),
            merge_sort(
                list_to_sort[split_index:],
            ),
        )

def merge_lists(list_a: List[int], list_b: List[int]) -> List[int]:
    merged = []
    while list_a and list_b:
        if list_a[0] < list_b[0]:
            merged.append(list_a.pop(0))
        else:
            merged.append(list_b.pop(0))
    if list_a:
        merged.extend(list_a)
    elif list_b:
        merged.extend(list_b)
    return merged


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

if __name__ == '__main__':
    large_list = list(range(10_000))
    large_list_copy = large_list.copy()
    random.shuffle(large_list_copy)
    merge_sort(large_list_copy)
