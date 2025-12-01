import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(tasks: List[int]) -> List[PairedTasks]:
    tasks.sort()
    return [(a,b) for a,b in zip(tasks[:len(tasks)//2], tasks[len(tasks)-1:len(tasks)//2-1:-1])]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
