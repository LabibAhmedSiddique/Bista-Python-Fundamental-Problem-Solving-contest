n = int(input())
s = set(map(int, input().split()))
Num_cmd = int(input())

for i in range(Num_cmd):
    x = input().split()

    if x[0] == "discard":
        s.discard(int(x[1]))
    elif x[0] == "remove":
        s.remove(int(x[1]))
    else:
        s.pop()

print(sum(s))
