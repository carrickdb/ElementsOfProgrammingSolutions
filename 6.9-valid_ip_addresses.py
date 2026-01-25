from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    def valid_octet(s):
        return len(s) != 0 and int(s) <= 255 and not (s[0]=="0" and len(s)!=1)
    ans = []
    for i in range(3):
        first = i+1
        if not valid_octet(s[:first]):
            continue
        for j in range(3):
            second = i+j+2
            if not valid_octet(s[first:second]):
                continue
            for k in range(3):
                third = i+j+k+3
                if not valid_octet(s[second:third]) or not valid_octet(s[third:]):
                    continue
                ans.append('.'.join([s[:first], s[first:second], s[second:third], s[third:]]))
    return ans
    

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
