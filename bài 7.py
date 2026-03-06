a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

if a == 0:
    if b == 0:
        print("Vô số nghiệm")
    else:
        print("Vô nghiệm")
else:
    x = -b / a
    print("x =", x)
