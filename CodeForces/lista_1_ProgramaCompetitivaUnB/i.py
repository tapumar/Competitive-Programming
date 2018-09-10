linhas, colunas = input().split()
linhas = int(linhas)
colunas = int(colunas)
m = []
check = 0
ind_s = []
ind_l = []
for i in range(linhas):
    m.append(input())

for c in range(len(m)):
    for l in range(len(m[c])):
        if m[c][l] == "1":
            check = 1
            ind_s.append(c)
            ind_l.append(l)
try:
    min_s = min(ind_s)
except:
    min_s = 0
try:
    max_s = max(ind_s)
except:
    max_s = 0
try:
    min_l = min(ind_l)
except:
    min_l = 0
try:
    max_l = max(ind_l)
except:
    max_l = 0
lim_l = max_l-min_l
lim_s = max_s-min_s
if check == 1:
    lim_s = lim_s + 1
    lim_l = lim_l + 1
print(str(lim_l)+"x"+str(lim_s))
