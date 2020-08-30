from collections import namedtuple
import math

Range = namedtuple('Range', ('min', 'max'))
n = 10 # number of intervals


def get_integral_squares(function, range_, n):
    """
    Method of squares.
    """
    step = (range_.max - range_.min) / n
    interval_values = [v/n * (range_.max - range_.min) + range_.min for v in range(n)]
    fn_values = [function(x) for x in interval_values]
    return step * sum(fn_values)

print(get_integral_squares(lambda x: x**3, Range(0, 2), 1000))


def get_integral_trapeze(function, range_, n):
    """
    Trapeze method.
    """
    step = (range_.max - range_.min) / n
    interval_values = [v/n * (range_.max - range_.min) + range_.min for v in range(n)]
    fn_values = [function(x) for x in interval_values]
    sum_ = 0
    for i in range(len(fn_values[:-1])): # skip at last element
        sum_ += fn_values[i] + fn_values[i+1]

    return step * sum_ / 2


print(get_integral_trapeze(lambda x: x**3, Range(0, 2), 100000))
