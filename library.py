import random


def make_array(length, array_range = (0, 100)):
    array  = []
    for i in range(length):
        array += [random.randint(array_range[0], array_range[1])]
    return array

def make_float_array(length, array_range = (0, 100)):
    array  = []
    for i in range(length):
        array += [random.randint(array_range[0], array_range[1]) + random.random()]
    return array