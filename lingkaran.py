import math

luas_lingkaran = lambda r: math.pi * r**2

r = float (input ("Masukan Radius = "))
area = luas_lingkaran (r)
print(f"Luas Lingkaran {r} adalah: {area:.2f}")