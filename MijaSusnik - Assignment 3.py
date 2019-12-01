import math

n=int(input("Enter number of poligon points: "))
print()

x=[]
y=[]

for r in range(n):
    print(f"Point {r+1}")
    Px=float(input("Enter x coordinate: "))
    Py=float(input("Enter y coordinate: "))
    print()

    x.append(Px)
    y.append(Py)

print()
print(f"{'':10} {'x':>7} {'y':>10}")
print("-" *30)

for r in range(n):
    print(f"Point {r+1} {x[r]: 10.2f} {y[r]: 10.2f}")

print()
print("Geometric characteristics:")

x.append(x[0:n][0])
y.append(y[0:n][0])

A=0
for i in range(n):
    A = A + ((x[i+1] + x[i]) * (y[i+1] - y[i]))
As = 0.5 * A
print(f"As = {As: .2f}")

S=0
for i in range(n):
    S = S + ((x[i+1] - x[i]) * (y[i+1]**2 + y[i] * y[i+1] + y[i]**2))
Sx = -1/6 * S
print(f"Sx = {Sx: .2f}")

S=0
for i in range(n):
    S = S + ((y[i+1] - y[i]) * (x[i+1]**2 + x[i] * x[i+1] + x[i]**2))
Sy = 1/6 * S
print(f"Sy = {Sy: .2f}")

I=0
for i in range(n):
    I = I + ((x[i+1] - x[i]) * (y[i+1]**3 + y[i+1]**2 * y[i] + y[i+1] * y[i]**2 + y[i]**3))
Ix = -1/12 * I
print(f"Ix = {Ix: .2f}")

I=0
for i in range(n):
    I = I + ((y[i+1] - y[i]) * (x[i+1]**3 + x[i+1]**2 * x[i] + x[i+1] * x[i]**2 + x[i]**3))
Iy = 1/12 * I
print(f"Iy = {Iy: .2f}")

I=0
for i in range(n):
    I = I + ((y[i+1] - y[i]) * (y[i+1] * (3 * x[i+1]**2 + 2 * x[i+1] * x[i] + x[i]**2) + y[i] * (3 * x[i]**2 + 2 * x[i+1] * x[i] + x[i+1]**2)))
Ixy = -1/24 * I
print(f"Ixy = {Ixy: .2f}")

xT = Sy / As
print(f"xT = {xT: .2f}")

yT = Sx / As
print(f"yT = {yT: .2f}")

IxT = Ix - yT**2 * As
print(f"IxT = {IxT: .2f}")

IyT = Iy - xT**2 * As
print(f"IyT = {IyT: .2f}")

IxyT = Ixy + yT * yT * As
print(f"IxyT = {IxyT: .2f}")