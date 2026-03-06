@@ -0,0 +1,18 @@
d,m,y = map(int,input("Nhap ngay thang nam: ").split())

days = [31,28,31,30,31,30,31,31,30,31,30,31]

if (y%4==0 and y%100!=0) or y%400==0:
    days[1] = 29

d += 1

if d > days[m-1]:
    d = 1
    m += 1

if m > 12:
    m = 1
    y += 1

print("Ngay mai:", d,"/",m,"/",y)
