from typing import List

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    p = A[pivot_index]
    l, h = 0, len(A)-1
    s1, s2 = l, h
    while l < h:
        if A[l] < p:
            l += 1
        elif A[h] > p:
            h -= 1
        elif A[h] < p and A[l] > p:
            tmp = A[h]
            A[h] = A[l]
            A[l] = tmp
            h -= 1
            l += 1
        elif A[l] == p:
            if s1 <= l:
                s1 = l+1
            while s1 < s2 and A[s1] == p:
                s1 += 1
            if s1 >= s2:
                break
            A[l] = A[s1]
            A[s1] = p
        elif A[h] == p:
            if s2 >= h:
                s2 = h-1
            while s2 > s1 and A[s2] == p:
                s2 -= 1
            if s2 <= s1:
                break
            A[h] = A[s2]
            A[s2] = p
        else:
            print("???")
            exit()

A = [0, 1, 1, 2]
pi = 2
A = [1, 0, 2, 0, 2, 1, 2, 1, 2, 0, 0, 0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 2, 1, 0, 2, 1, 2, 0, 2, 1, 1, 2, 2, 0, 1, 1, 0, 1, 1, 1, 2, 1, 0, 1, 2, 1, 2, 1, 2, 2, 2, 0, 1, 0, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 0, 2, 0, 1, 2, 1, 1, 1, 0, 2, 0, 1, 2, 1, 1, 2, 1, 2, 2, 1, 0, 1, 2, 2, 1, 2, 2, 1, 1, 2, 0, 1, 0, 1, 2, 0, 2, 1, 2, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0]
pi = 101
# A = [1,5,9,5,5,1,9,1,1,5,5,1,1]
# pi = 1
# A = [3,1,2]
# pi = 2
dutch_flag_partition(pi, A)
print(A)