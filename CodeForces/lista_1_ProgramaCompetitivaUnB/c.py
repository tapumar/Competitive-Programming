n = input()
vetor = input().split()
max_diff = 0
for i in range(len(vetor)-1):
    diff = abs(int(vetor[i]) - int(vetor[i+1]))
    if diff > max_diff:
        max_diff = diff
print(max_diff)
