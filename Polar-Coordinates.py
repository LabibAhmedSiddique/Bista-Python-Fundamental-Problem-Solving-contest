import cmath

x = complex(input().strip())
pol_cord = cmath.polar(x)

print(pol_cord[0])
print(pol_cord[1])
