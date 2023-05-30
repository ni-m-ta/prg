import sys
A,B,C,X,Y = map(int, input().split())
sum = sys.maxsize

if X < Y:
    for c in range(0,2*(Y+1),2):
        if X-c/2 < 0:
            if sum > C*c + B*(Y-c/2):
                sum = C*c + B*(Y-c/2)
        else:
            if sum > C*c + A*(X-c/2) + B*(Y-c/2):
                sum = C*c + A*(X-c/2) + B*(Y-c/2)
else:
    for c in range(0,2*(X+1),2):
        if Y-c/2 < 0:
            if sum > C*c +A*(X-c/2):
                sum = C*c +A*(X-c/2)
        else:
            if sum > C*c + A*(X-c/2) + B*(Y-c/2):
                sum = C*c + A*(X-c/2) + B*(Y-c/2)

print(int(sum))