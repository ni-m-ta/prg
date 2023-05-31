N = int(input())
S = input()
nums = set([])

I = [True for _ in range(10)]
for i in range(N-2):
    if I[int(S[i])]:
        I[int(S[i])] = False
        J = [True for _ in range(10)]
        for j in range(i+1,N-1):
            if J[int(S[j])]:
                J[int(S[j])] = False
                for k in range(j+1,N):
                    nums.add(S[i]+S[j]+S[k])

print(len(nums))