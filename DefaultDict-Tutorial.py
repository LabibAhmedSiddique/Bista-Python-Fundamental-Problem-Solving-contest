from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    x = input()
    d[x].append(i+1)

for i in range(m):
    z = input()

    if z in d:
        print(' '.join(map(str, d[z])))
    else:
        print("-1")
