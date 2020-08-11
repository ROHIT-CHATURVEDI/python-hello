a =48
b=6
print(a+b) # 14 .
print(a-b) # 2 .
print(a*b) # 48 .
print(a / b) # 1.3 rounded off.
print(a // b)   # integer division :- 1 .
print(a % b)  # remainder :- 2 (Modulo operator).

print()
for i in range(1,a//b):
    print(i)


print("\n\n")
bun_price = 2.40
money = 15
total = money//bun_price
print(total)

# Starting Operator Precedence.
print("\n\n\n\n")
print(a * (b+a)) # a = 48 , b = 6 , result  = 2592.
print(a + (b * (a - b) - b) * a)
# 48 + ( 6 * (48 - 6) - 6 ) * 48 )

print( "\n")
print("We can also do in this way :- ")
e = a - b
f = e * 6
g = f - 6
h = g * 48
i = h + 48
print(i)