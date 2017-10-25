import sys
from collections import OrderedDict

nomes = []
ordem = {}
for line in sys.stdin:
    line = line.strip()
    nomes.append(line.lower())
    ordem[line.lower()] = line
nomes.sort()
print(ordem[nomes[-1]])
