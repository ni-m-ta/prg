s = input()
tmp = 0
ans = 0
wasIn = False
for i in range(len(s)):
    if s[i] in ('A','C','G','T'):
        tmp += 1
    else:
        if ans < tmp:
            ans = tmp
        tmp = 0
    if i == len(s)-1 and ans < tmp:
        ans = tmp

print(ans)