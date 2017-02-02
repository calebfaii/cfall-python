# Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
# and D = |Pk - Pj| is minimised; what is the value of D?

import itertools


def get_pentagonal(low, high):

    """Returns the first n pentagonal numbers."""

    pentagonal_list = []
    for i in range(low, high):
        pentagonal = (i * ((3 * i) - 1)) / 2
        pentagonal_list.append(pentagonal)
    return pentagonal_list


def iterate_sums(p_list):

    """Receives a list of pentagonal numbers; returns pairs whose sum is pentagonal."""

    psum_list = []
    for i in itertools.combinations(p_list, 2):
        isum = sum(i)
        if isum in p_list:
            psum_list.append(i)
    if len(psum_list) == 0:
        return "No s-list in this range."
    else:
        return psum_list


def iterate_difference(sum_list, p_list):

    """Receives a list of pairs; returns those pairs whose difference is pentagonal."""

    diff_list = []
    for i in sum_list:
        diff = abs(i[0] - i[1])
        if diff in p_list:
            diff_list.append(i)
    if len(diff_list) > 0:
        return diff_list
    else:
        return "No d-list in this range."


def try_difference(p_list):

    pdiff_list = []
    for i in itertools.combinations(p_list, 2):
        idiff = (i[1] - i[0])
        if idiff in p_list:
            pdiff_list.append(i)
    if len(pdiff_list) == 0:
        return "No s-list in this range."
    else:
        return pdiff_list

print try_difference(get_pentagonal(1, 100))


# while True:
#     x = int(raw_input('Start? :'))
#     y = int(raw_input('End? :'))
#     pent_list = get_pentagonal(x, y)
#     slist = iterate_sums(pent_list)
#     dlist = iterate_difference(slist, pent_list)
