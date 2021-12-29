import sys

read = sys.stdin.readline

# 1 <= M <= N <= 7
N,M = list(map(int, read().split()))

s= []
def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        s.append(i)
        dfs()
        s.pop()

dfs()
