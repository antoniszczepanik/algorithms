from typing import List
import random
import time


def count_inversions(list_to_count: List[int]) -> List[int]:
    if len(list_to_count) <= 1:
        return list_to_count, 0

    elif len(list_to_count) == 2:
        if list_to_count[0] > list_to_count[1]:
            return list_to_count[::-1] , 1
        else:
            return list_to_count, 0
    else:
        split_index = len(list_to_count) // 2
        count_inversions
        left_sorted, inv_number_left = count_inversions(
                list_to_count[:split_index],
            )
        right_sorted, inv_number_right = count_inversions(
                list_to_count[split_index:],
            )
        new_sorted, new_inversions = merge_lists(right_sorted, left_sorted)
        return new_sorted, inv_number_left + inv_number_right + new_inversions

def merge_lists(list_a: List[int], list_b: List[int]) -> List[int]:
    merged = []
    inversions_count = 0
    while list_a and list_b:
        if list_a[0] < list_b[0]:
            merged.append(list_a.pop(0))
        else:
            merged.append(list_b.pop(0))
            inversions_count += len(list_a)

    if list_a:
        merged.extend(list_a)
    elif list_b:
        merged.extend(list_b)
    return merged, inversions_count

if __name__ == '__main__':

    large_list = list(range(9999))
    large_list_copy = large_list.copy()
    random.shuffle(large_list_copy)
    start = time.time()
    _, inversions_number = count_inversions(large_list_copy)
    print('counted_inverstions in', time.time() - start)
    print('inversion number', inversions_number)


    start = time.time()
    _, inversions_number = count_inversions([5, 3, 8, 1])
    print('counted_inverstions in', time.time() - start)
    print('inversion number', inversions_number)
