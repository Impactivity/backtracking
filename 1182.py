import sys
from itertools import combinations

read = sys.stdin.readline
n,s = map(int , read().split())
arr = list(map(int , read().split()))

# cnt = 0
# for i in range(1 , n+1):
#     ans = list(combinations(arr,i))
#     for tmp in ans:
#         if sum(tmp) == s :
#             cnt += 1
#
#
#
# print(cnt)

cnt = 0
def dfs(inx, sub_sum):
    global cnt

    if inx >= n :
        return

    sub_sum += arr[inx]

    if sub_sum == s:
        cnt += 1

    dfs(inx+1 , sub_sum)

    dfs(inx+1, sub_sum - arr[inx])


dfs(0,0)
print(cnt)