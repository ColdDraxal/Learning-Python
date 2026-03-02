import math
a=23.967
b=3.14
# print(f"{a*b:.2f}")
# print(f"{math.pi:.2f}")

# :.2f limits the after decimal digits to 2 digits. amount can be adjusted eg: .8f

print(f"{a=} {b=} {a+b=}")

# shows both variable and values

c= "Rs"
d= "100"
print(f"I have {c:<10} {d:^10}")
# :> right allignment, :< left allignment , :^ top allignment
"""
e=26
print(f"{math.pi:>{e}.2f}")

"""

for i in range(5, 20, 3):
    print(f"{math.pi:>{i}.2f}")