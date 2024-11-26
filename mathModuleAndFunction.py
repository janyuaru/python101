# อ่านจำนวนเต็มจาก input มาเก็บใน m
# อ่านจำนวนเต็มจาก input มาเก็บใน k
# นำค่าใน k ไปเพื่มให้กับตัวแปร m
m = int(input())
k = int(input())
m += k

# อ่านสตริงจาก input เก็บใน s
# อ่านสตริงจาก input เก็บใน t
# นำสตริงใน t ไปต่อทางขวาของ s
s = str(input())
t = str(input())
s += t

# อ่านจำนวนจริงจาก input มาเก็บใน d
#    d เป็นมุม หน่วยเป็นองศา
# ให้ r เก็บค่ามุมหน่วยเรเดียนที่แปลงจาก d
# ให้ x เก็บค่า sin( r )
# ให้ y เก็บค่าเดียวกับ x 
#    แต่ปัดเศษให้มีเลขหลังจุดทศนิยม 2 ตำแหน่ง
#
import math
d = float(input())
r = math.radians(d)
x = math.sin(r)
y = round(x, 2)