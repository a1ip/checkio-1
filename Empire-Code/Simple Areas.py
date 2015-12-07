'''
use hero's formula for triangle area
'''

def simple_areas(*args):
    from math import pi, sqrt
    if len(args) == 1:
        return pi * args[0] * args[0] / 4
    elif len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 3:
        p = sum(args) / 2
        return sqrt(p * (p-args[0]) * (p-args[1]) * (p-args[2]))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

    print("Earn cool rewards by using the 'Check' button!")
