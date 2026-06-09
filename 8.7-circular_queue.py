from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.q = [None for _ in range(capacity)]
        self.beg = 0
        self.end = 0

    def enqueue(self, x: int) -> None:
        self.q[self.end] = x
        self.end = (self.end+1) % len(self.q)
        if self.end == self.beg:
            newq = self.q[self.beg:]
            newq.extend(self.q[:self.end])
            newq.extend([None for _ in range(len(self.q))])
            self.end = len(self.q)
            self.q = newq
            self.beg = 0

    def dequeue(self) -> int:
        ret = self.q[self.beg]
        self.beg = (self.beg + 1) % len(self.q)
        return ret

    def size(self) -> int:
        if self.beg > self.end:
            return len(self.q) - self.beg + self.end
        return self.end - self.beg


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))

# queue_tester([["Queue", 1], ["enqueue", 1], ["enqueue", 2], ["dequeue", 1], ["dequeue", 2], ["enqueue", 3], ["enqueue", 4], ["enqueue", 5], ["size", 3]])

# queue_tester([["Queue", 1], ["enqueue", -394], ["enqueue", -304], ["dequeue", -394], ["enqueue", -65], ["dequeue", -304], ["dequeue", -65], ["enqueue", 513], ["dequeue", 513], ["size", 0]])