import sys
read =sys.stdin.readline

n,m = map(int,read().split())

numbers = list(map(int,read().split()))
numbers.sort()

cnt = 0

arr = []
visited = [0]*n

def back_tracking(depth,arr,visited):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(depth,len(numbers)):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(numbers[i])
            back_tracking(depth,arr,visited)
            visited[i] = 0
            arr.pop()

back_tracking(0,arr,visited)