import sys
read = sys.stdin.readline

# | a[0]-a[1] | +  | a[1] - a[2] | + ... + |a[n-2] - a[n-1]| 의 최댓값

n = int(read())
arr = list(map(int , read().split()))

s = []
answer = []
visited = [0] * n

def dfs(depth):
    if depth == n:
        answer.append(sum(abs(s[i] - s[i+1]) for i in range(n-1)))
        return

    for i in range(0,n):
        if visited[i] == 0:
            s.append(arr[i])
            visited[i] = 1
            dfs(depth+1)
            s.pop()
            visited[i] = 0

dfs(0)
print(max(answer))
