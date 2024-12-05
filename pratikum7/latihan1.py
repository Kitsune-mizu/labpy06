import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))

print("hasil a(5):", a(5)) # menghitung kuadrat dari 5
print("hasil b(3, 4):", b(3, 4)) # nilai pythagoras 
print("hasil c(1, 2, 3, 4, 5):", c(1, 2, 3, 4, 5)) # mencari nilai rata-rata/pertengahan
print("hasil d('hello'):", d("hello")) # kata acak dari string "hello"
