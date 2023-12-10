x = 15
y = 20

print("x", x)
print("y", y)
# Основные операции
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x % y =", x % y)
print("x // y =", x // y)
y = 2
print("x ** y =", x ** y)

# Битовые операции
x = 25
y = 7

print("x=", x ,' = ', bin(x))  # Двоичная система счисления
print("x=", x ,' = ', hex(x))  # Десятиричная система счисления
print("x=", x ,' = ', oct(x))  # Восьмиричная система счисления
print("x | y ", bin(x | y) ,"y | x ", bin(y | x))  # Побитовое или
print("x & y ", bin(x & y) ,"y & x ", bin(y & x))  # Побитовое и
print("x ^ y ", bin(x ^ y) ,"y ^ x ", bin(y ^ x))  # Исключающее или
print(" ~ x ",  bin(~x))  # Отрицание
print(" x << 1 ",  bin(x << 1))  # Сдвиг на 1 влево
print(" x >> 1 ",  bin(x >> 1))  # Сдвиг на 1 вправо