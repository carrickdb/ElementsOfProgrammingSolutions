from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    v = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s = [(i,j,0)]
            while s:
                curr = s.pop()
                if curr in v:
                    continue
                v.add(curr)
                ci,cj,pattern_i = curr
                if pattern[pattern_i] == grid[ci][cj]:
                    if pattern_i == len(pattern) - 1:
                        return True
                    for di,dj in [(0,1), (1,0),(-1,0), (0,-1)]:
                        ni,nj = ci+di, cj+dj
                        if ni < 0 or ni >= len(grid):
                            continue
                        if nj < 0 or nj >= len(grid[0]):
                            continue
                        s.append((ni,nj, pattern_i+1))
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
