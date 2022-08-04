from collections import Counter
x = int(input())
stk = list(map(int, input().split(" ")))
n = int(input())
shoe_stk = (Counter(stk))
total_price = 0
for i in range(n):
    size, price = map(int, input().split(' '))
    if shoe_stk[size]:
        shoe_stk[size] -= 1
        total_price = total_price+price
print(total_price)
