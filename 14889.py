# N / 2 명이 한팀을 이룬다.
# 각 팀원들의 합이 팀의 능력치이고 두 팀의 능력치 차이가 최솟값을 이뤄야함.

import sys
read = sys.stdin.readline

n = int(read())
graph = [ list( map(int , read().split()) )for _ in range(n) ]

visited=[ 0  for _ in range(n) ]
result=[]

min_result = 100000000

def dfs(cnt,inx):
    global min_result

    if cnt == n // 2:
        print('통과')
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] == 1 and visited[j] == 1:
                    start += graph[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    link += graph[i][j]
        min_result = min(min_result , abs(start-link))
    print(visited)
    print(' ')
    for i in range(inx, n):
        if visited[i] == 0 :
            visited[i] = 1
            dfs(cnt + 1 , i + 1)
            visited[i] = 0


dfs(0,0)
print(min_result)