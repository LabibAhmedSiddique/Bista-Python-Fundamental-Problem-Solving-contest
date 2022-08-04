e_r = int(input())
Eng = set(map(int, input(
).strip().split()))
f_r = int(input())
fren = set(map(int, input(
).strip().split()))


print(len(Eng.difference(fren)))
