from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    smaller = min(n,m)
    larger = max(m,n)
    dp = [1 for _ in range(smaller)]
    for i in range(larger-1):
        newdp = []
        for j in range(smaller):
            if j == 0:
                newdp.append(1)
            else:
                newdp.append(newdp[-1] + dp[j])
        dp = newdp
    return dp[-1]

# print(number_of_ways(1,1))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
