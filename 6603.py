import sys
read = sys.stdin.readline


# dfs 호출 순서는 아래와 같이 될 것이다.
# 입력 : 7 1 2 3 4 5 6 7
#
#           visited
# Dfs(0,0) 1
# Dfs(1,1) 1 2
# Dfs(2,2) 1 2 3
# Dfs(3,3) 1 2 3 4
# Dfs(4,4) 1 2 3 4 5
# Dfs(5,5) 1 2 3 4 5 6  Return
# dfs(5,5) 1 2 3 4 5 7 return
# Dfs(4,4) 1 2 3 4 6
# Dfs(5,5) 1 2 3 4 6 7 return
# dfs(4,4) 1 2 3 4 7
# dfs(5,5) 1 2 3 4 7 6  return
# dfs(4,4) return
# Dfs(3,3) 1 2 3 5
# dfs(4,4) 1 2 3 5 6
# dfs(5,5) 1 2 3 5 6 7 return
# .
# .
# .



visited = [0 for i in range(13)]

def dfs(inx, depth):
    if depth == 6:
        for i in range(6):
            print(visited[i], end=' ')
        print()
        return

    # vidited 배열에 depth번째의 값을 graph i번쨰 값으로 바꾸고 재귀 호출하는게 포인트임
    # 재귀 돌면 inx부터 끝까지 visited에 값을 채워 넣기 때문에 가능한 경우의 수를 모두 돈다.
    for i in range(inx, len(graph)):
        visited[depth] = graph[i]
        dfs(i+1, depth+1)


while True:
    graph = list(map(int,read().split()) )
    if graph[0] == 0 :
        break
    del graph[0] #맨 첫 번째 갯수를 의미하는 수는 지움.
    dfs(0)
    print()

