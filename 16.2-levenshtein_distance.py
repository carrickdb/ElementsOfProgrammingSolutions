from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    la = len(A)
    lb = len(B)
    if la < lb:
        smaller = A
        larger = B
    else:
        smaller = B
        larger = A

    dp = [i for i in range(len(smaller)+1)]
    # print(dp)
    for i in range(len(larger)):
        newdp = []
        for j in range(len(smaller)+1):
            if j == 0:
                newdp.append(dp[0] + 1)
                continue
            # print(i, A[i-1], j, B[j-1])
            if larger[i] == smaller[j-1]:
                newdp.append(dp[j-1])
            else:
                newdp.append(min(dp[j], newdp[-1], dp[j-1]) + 1)
        dp = newdp
        # print(dp)
    return dp[-1]

a = "GCTACACGCAGTTGCCTCGAGGAAACAAGCGCAATCGGATCGCGCATCCACACCACGACCCTGTAA"
b = "GGGGATTCGGCATGGCGTAGGGGAATTGCTGAACGACACTCGTGCATTTAAGGGGGAACTATTACAG"
a = "Saturday"
b = "Sundays"
# a = "GCTCCCGCACGTCCCC"
# b = "AGTCCCGTATAGAGACATACGCAGAGGCATAAATCCCAGCTGTATTCTCCGTAGAATGCTACTGCG"
# a = "Carthorse"
# b = "Orchestra"
# print(levenshtein_distance(a, b))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
