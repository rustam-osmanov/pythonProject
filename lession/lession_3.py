age = 30  # integer  инициализация переменной возраста
name = 'Rustam'  # string инициализация переменной имени
height = 172.58  # float инициализация переменной Рост
isExist = True  # boolean

print("Имя", name);
print("Возраст " + str(age)) # Вывод переменной с приведением в тип строки

print("Возраст", age) # Вывод переменных разных типов
print("Рост", height, 'см')
print("Есть", isExist)
isExist = False  # boolean
print("Есть", isExist)

print("Тип переменной age", type(age))
print("Тип переменной name", type(name))
print("Тип переменной height", type(height))
print("Тип переменной isExist", type(isExist))
"""
Выодим несколько строк с переходом
и этот тест 
является многострочным комментарием
"""
text = 'Первая строка\nВторая строка\nТретья строка' # вывод строк с переходом на новую строку
print(text)
text2 = '''Строка 1
Строка 2
Строка 3''' # вывод строк с переходом без использования \n и вместо ' можно использовать "
print(text2)
