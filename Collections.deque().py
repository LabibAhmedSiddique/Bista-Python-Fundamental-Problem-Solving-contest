from collections import deque

N = int(input())
d = deque()

for i in range(N):
    x = input().split()
    # print(x[1])
    if (x[0]) == "append":
        d.append(int(x[1]))
        # print(d)
    elif (x[0]) == "pop":
        d.pop()
    elif (x[0]) == "appendleft":
        d.appendleft(int(x[1]))

    else:
        d.popleft()

print(*[item for item in d])
