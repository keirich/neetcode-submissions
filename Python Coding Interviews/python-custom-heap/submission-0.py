import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    h = []
    l = []
    for i in nums:
        heapq.heappush(h, (-i, i))
    while h:
        l.append(heapq.heappop(h)[1])
    return l



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
