arr = []

# 1 부터 9까지의 자연수
for i in range(1,10):
    arr.append(i)

# 백트래킹을 활용하여 무작위로 2개를 뽑는 경우의수 출력
def dfs():
    if len(s) == 2:
        print(' '.join(map(str,s)))
        return
    for i in range(0, len(arr)):
        if visited[i] == 0:
            visited[i] = 1
            s.append(arr[i])
            dfs()
            s.pop()
            visited[i] = 0

s = []

visited = [0] * len(arr)

dfs()
