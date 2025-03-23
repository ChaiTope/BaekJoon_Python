import math
from functools import reduce


def lcm_multiple(numbers):
    return reduce(math.lcm, numbers)