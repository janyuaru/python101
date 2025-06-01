#มีตัวแปร text เก็บสตริงอยู่แล้ว ถ้าใน text มี Python หรือ python ปรากฏอยู่ให้แสดง Yes ไม่เช่นนั้นแสดง No
if 'Python' in text or 'python' in text:
    print("Yes")
else:
    print("No")

#มีตัวแปร month เก็บสตริงอยู่แล้ว ถ้า month เก็บชื่อเดือน ให้แสดง Yes ไม่เช่นนั้นก็แสดง No ชื่อเดือนมีดังนี้ January, February, March, April, May, June, July, August, September, October, November, December
if month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    print("Yes")
else:
    print("No")
