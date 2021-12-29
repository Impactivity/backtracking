import sys

read = sys.stdin.readline

N,M = list(map(int, read().split()))

s= []
def dfs(k):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        if k <= i:
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)

