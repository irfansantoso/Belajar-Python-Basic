#if statment standard
nilai = 85

if nilai >= 90:
    print("Nilai A")
elif nilai >= 80: # sama dengan else if
    print("Nilai B")
else:
    print("Nilai C")

#dengan operator ternary
a = 80
x = 0 if a < 70 else 1
print(x)