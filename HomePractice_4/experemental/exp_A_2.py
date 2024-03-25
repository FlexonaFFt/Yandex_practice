def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    k = int(input())
    for _ in range(k):
        l, r = map(int, input().split())
        lower = bisect.bisect_left(a, l)
        upper = bisect.bisect_right(a, r)
        print(upper - lower)

import bisect
main()