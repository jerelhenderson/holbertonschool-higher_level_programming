#!/usr/bin/python3
"""
find peak in list of unsorted ints
"""


def find_peak(list_of_integers):
    """
    locate highest peak
    """
    nums = list_of_integers
    length = len(list_of_integers)

    if length is None:
        return None

    beg = 0
    end = length - 1
    mid = length // 2

    while beg <= end:
        if nums[mid] >= nums[mid - 1] and nums[mid] >= nums[mid + 1]:
            return nums[mid]
        elif nums[mid - 1] >= nums[mid]:
            mid = mid - 1
            end = mid
        elif nums[mid + 1] >= nums[mid]:
            mid = mid + 1
            big = mid
