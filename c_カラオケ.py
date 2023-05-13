n,m = map(int,input().split())
scores = {}
sum_scores = []
for i in range(n):
    scores[i] = list(map(int,input().split()))

for i in range(m-1):
    for j in range(i+1,m):
        sum_score = 0
        for k in range(n):
            if scores[k][i] > scores[k][j]:
                sum_score += scores[k][i]
            else:
                sum_score += scores[k][j]
        sum_scores.append(sum_score)

print(max(sum_scores))