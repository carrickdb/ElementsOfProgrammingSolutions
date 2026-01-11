from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    first_part = []
    second_part = []
    minprice = float("inf")
    maxsofar = float("-inf")
    for p in prices:
        minprice = min(minprice, p)
        maxsofar = max(maxsofar, p-minprice)
        first_part.append(maxsofar)
    maxprice = float("-inf")
    maxsofar = float("-inf")
    for i in range(len(prices)-1, -1, -1):
        maxprice = max(maxprice, prices[i])
        maxsofar = maxprice - prices[i]
        second_part.append(maxsofar)
    second_part = second_part[::-1]
    ans = float("-inf")
    for i in range(len(prices)):
        # print(i, first_part[i], second_part[i], first_part[i]+second_part[i])
        ans = max(ans, first_part[i]+second_part[i])
    return ans

# print(buy_and_sell_stock_twice([1,2,5,3,10,8,2,20,4]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
