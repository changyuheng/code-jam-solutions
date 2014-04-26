# -*- coding: utf-8 -*-

import sys


def solve():
    N, L = map(int, input().split())
    os = sorted(int(i, 2) for i in input().split())
    ds = sorted(int(i, 2) for i in input().split())
    ans = L + 1

    for d in ds:
        if sorted(os[0] ^ d ^ o for o in os) == ds:
            ans = min(ans, bin(os[0] ^ d).count('1'))

    if ans > L:
        ans = 'NOT POSSIBLE'

    return ans

def main():
    T = int(input())
    for i in range(1, T + 1):
        print('Case #{}: {}'.format(i, solve()))

if __name__ == '__main__':
    sys.exit(main())
