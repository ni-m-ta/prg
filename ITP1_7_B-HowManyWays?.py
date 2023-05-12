# input_list = []
# counters = []
# while True:
#     n,x = map(int,input().split())
#     if n == 0 and x == 0:
#         break
#     input_list.append([n,x])

# for i in range(len(input_list)):
#     counter = []
#     n = input_list[i][0]
#     x = input_list[i][1]
#     for j in range(1,n+1):
#         for k in range(1,n+1):
#             for l in range(1,n+1):
#                 if j + k + l == x and j != l and l != k and k != j:
#                     nums = sorted([j,k,l])
#                     if nums not in counter:
#                         counter.append(nums)
#     counters.append(len(counter))

# for i in range(len(counters)):
#     print(counters[i])

# naoto172

import sys
BIG_NUM = 2000000000

while True:
    n,x = map(int,input().split())
    if n == 0 and x == 0:
        break
    ans = 0
    for i in range(1,n-1):
        for k in range(i+1,n):
            p = x-(i+k)
            if p < 0 or p > n:
                continue
            if p > k:
                ans += 1
    print(ans)