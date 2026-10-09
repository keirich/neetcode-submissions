from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    o = -1
    for i,n in enumerate(nums):
        if n == 7 and o == -1:
            o = i
    return o



def get_dist_between_sevens(nums: List[int]) -> int:
    f = -1
    s = -1
    for i,n in enumerate(nums):
        if n == 7:
            if f == -1:
                f = i
            elif s == -1:
                s = i
    return s - f


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
