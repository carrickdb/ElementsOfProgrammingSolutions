from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    dp = [[0 for _ in range(final_score+1)] for _ in range(len(individual_play_scores)+1)]
    dp[0][0] = 0
    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            if j == 0:
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i-1][j]
            score = individual_play_scores[i-1]
            if j>=score:
                dp[i][j] += dp[i][j-score]
    return dp[-1][-1]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
