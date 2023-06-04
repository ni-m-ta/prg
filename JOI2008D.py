m = int(input())
ms = [list(map(int, input().split())) for _ in range(m)]
n = int(input())
ns = [list(map(int, input().split())) for _ in range(n)]
found = False
pi = 0

while not found:
    pivot_x, pivot_y = ns[pi][0]-ms[0][0], ns[pi][1]-ms[0][1]
    does_seek = True
    for i in range(1,m):
        if not does_seek: break
        for j in range(n):
            if j == pi: continue
            if ns[j][0]-ms[i][0]==pivot_x and ns[j][1]-ms[i][1]==pivot_y:
                does_seek = True
                break
            else:
                does_seek = False
        if i == m-1 and does_seek:
            does_seek = False
            found = True
    pi += 1

print(str(pivot_x)+" "+str(pivot_y))