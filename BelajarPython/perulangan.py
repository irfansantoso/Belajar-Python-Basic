# for index in range():
    # action
    # action juga
# diluar for

for i in range(5):
    print(i)
print("\n")

for z in range(3):
    print("Perulangan ke-"+str(z+1)) # klo gk pake text perulangan, gk perlu pake str(), langsung aja z+1
print("\n")

for x in range(3):
    print("#" * (x+1))
print("\n")

for k in range(3):
    print(" "*(3-k-1) + "@"*(2*k+1))
print("\n")

for m in range(1,7):
    if m is 5:
        print("nilai adalah 5")
        #break
        continue
    print("nilai sekarang",m)
