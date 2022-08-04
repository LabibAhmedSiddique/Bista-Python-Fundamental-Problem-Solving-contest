n, m = map(int, input().split())
M = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happy = 0
A_List = list(A)
B_List = list(B)
for i in M:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1
print(happy)
