# รับสตริงจาก input เก็บในตัวแปร grade
# แสดงข้อความว่า I'll get ตามด้วยช่องว่าง 1 ช่อง
# ตามด้วยค่าในตัวแปร grade
#
grade = input()
print("I'll get", grade)

# รับจำนวนจริงจาก input เก็บในตัวแปร h
# รับจำนวนจริงจาก input เก็บในตัวแปร w
# h คือความสูงของสามเหลี่ยม
# w คือความยาวฐานของสามเหลี่ยม
# แสดงพื้นที่ของสามเหลี่ยม
#
h = float(input())
w = float(input())
print(1/2*w*h)

# รับจำนวนเต็มจาก input เก็บในตัวแปร x
# รับจำนวนเต็มจาก input เก็บในตัวแปร y
# คำนวณ x ยกกำลัง y เก็บใน z
# นำหลักหน่วยของ z เก็บใน d
# แสดงค่าของ d
#
x = int(input())
y = int(input())
z = x**y
d = z%10
print(d)

#พยายามทำความเข้าใจว่า ทำไมถึงได้ผลลัพธ์ดังที่แสดง
print("5 / 2 =", 5/2) #2.5
print("5 // 2 =", 5//2) #2

print("4**2 =", 4**2) #16
print("4**0.5 =", 4**0.5) #2.0

print("9 % 24 =", 9%24) #9
print("(9+24) % 24 =", (9+24)%24) #9

print("(-1+24) % 24 =", (-1+24)%24) #23
print("-1 % 24 =", -1%24) #23

print("4.5 % 1 =", 4.5%1) #0.5
 
print("int(4.9) =", int(4.9)) #4
print("int(-4.9) =", int(-4.9)) #-4

#เขียนคำสั่งที่แสดง สองหลักขวาสุดของค่า (21387)^2341
print( (21387**2341)%100 )

