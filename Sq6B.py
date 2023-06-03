import sys

n = int(input())
goods = [list(map(int,input().split())) for _ in range(n)]
min_time = sys.maxsize

for i in range(n):
    for j in range(n):
        start, end = goods[i][0], goods[j][1]
        time = 0
        for k in range(n):
            time += abs(start-goods[k][0]) + abs(goods[k][1]-goods[k][0]) + abs(end-goods[k][1])
        min_time = min(min_time, time)

print(min_time)
