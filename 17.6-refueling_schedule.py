import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20

# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance from city i to the next city.
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    smallest = float("inf")
    smallestCity = 0
    l = len(gallons)
    currGall = 0
    for i in range(l):
        if currGall < smallest:
            smallest = currGall
            smallestCity = i
        currGall += gallons[i]
        currGall -= distances[i]//MPG
    # return the index of the ample city
    print(smallestCity)
    return smallestCity


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('refueling_schedule.py',
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
