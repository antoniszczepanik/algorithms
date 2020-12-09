def count_sort(to_sort, vals_range):
    """ Assuming range of 1..10 """
    occurences = {k: 0 for k in range(vals_range)}
    for number in to_sort:
        if number >= vals_range:
            raise Exception("This range is riddiculus man...")
        occurences[number] += 1

    output = []
    for number, value in occurences.items():
        while value > 0:
            output.append(number)
            value -= 1

    return output


if __name__ == "__main__":
    to_sort = [1, 5, 2, 2, 4, 5, 9, 9, 9, 8, 13]
    print(count_sort(to_sort, 15))
