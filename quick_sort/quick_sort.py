import random
from collections import namedtuple

def quick_sort(to_sort):
    if len(to_sort) <= 1:
        return to_sort
    elif len(to_sort) == 2:
        if to_sort[0].number_value > to_sort[1].number_value:
            return [to_sort[1].number_value, to_sort[0].number_value]
        else:
            return to_sort

    pivot_ix = random.choice(range(len(to_sort)))
    pivot_value = to_sort[pivot_ix]
    smaller, larger = [], []
    for ix, number in enumerate(to_sort):
        if ix == pivot_ix:
            continue
        if number.number_value < pivot_value.number_value:
            smaller.append(number)
        elif number.number_value == pivot_value.number_value:
            # make sure order is saved when numbers are equal
            if ix < pivot_ix:
                smaller.append(number)
            else:
                larger.append(number)
        elif number.number_value > pivot_value.number_value:
            larger.append(number)

    return quick_sort(smaller) + [pivot_value] +  quick_sort(larger)

def quick_sort_permutations(to_sort):
    Number = namedtuple('number', ['number_value', 'original_index'])
    to_sort = [Number(number_value=v, original_index=i) for i, v in enumerate(to_sort)]
    return [num.original_index for  num in quick_sort(to_sort)]

large_list = [1, 2, 2, 3, 4, 5]
to_sort = large_list.copy()
random.shuffle(to_sort)
print(to_sort)
print(quick_sort_permutations(to_sort))
