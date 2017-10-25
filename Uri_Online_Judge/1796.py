pessoas = int(input())
sat = input().split()

sim = sat.count("0")
if sim > (len(sat)/2):
    print("Y")
else:
    print("N")
