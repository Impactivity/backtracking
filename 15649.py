import sys

# from itertools import permutations
#
read = sys.stdin.readline
N,M = map(int, read().split()) # 1 <= M <= N <= 8

#solution 1
#
# array = []
# for i in range(1,N+1):
#     array.append(i)
#
#
# answer = list( map(list, permutations(array, M) ))
#
# for i in range(0, len(answer)):
#     for j in range(0,M):
#         print(answer[i][j] , end = ' ')
#     print('')




# solution 2

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1,N+1):
        if i not in s:
            s.append(i)
            dfs()
            print('pop  : ' , s[-1])
            s.pop()

dfs()