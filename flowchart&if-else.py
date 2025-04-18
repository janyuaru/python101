a = int(input())
b = int(input())
if a < b :
    min = a
    max = b
else :
    min = b
    max = a
print(min, max)

if abs(a - b) > 2 :
    a,b = b,a
else :
    a = b**2 + a
print(a, b)

if a%2 == 0:  # a เป็นจำนวนคู่ ?
    a *= 2
else :
    if a > 10 :
        a //= 2
    else :
        a = 0
print(a)

if a%2 == 0:  # a เป็นจำนวนคู่ ?
    if a > 10:
        a //= 2
    else:
        a = 0
else:
    a *= 2
print(a)

if a % 2 == 0:
    b = 2*a
    if a > 10:
        a //= 2
    else:
        b += a
    a += b
else:
    a *= 2
print(a,b)
