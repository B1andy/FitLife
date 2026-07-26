# Проект FitLife - MVP версия 1.0

# Константы WATTER_PER_KG(рекомендация для поддержания водного баланса в мл.)

WATER_PER_KG = 30

# Приветсвенное сообщение

print("Добро пожаловать в FitLife!")

# Сбор данных о пользователе имя и возраст

user_name = input("Введите ваше имя: ")
user_age = int(input("Введите ваш возраст: "))

# Сбор данных пользователя вес и рост

user_weight = float(input("Введите ваш вес (кг): "))
user_height = float(input("Введите ваш рост (в метрах, например 1.75): "))

# Расчет индекса массы тела

bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Расчет рекомендуемой нормы воды

water_ml = user_weight * WATER_PER_KG
water_l = water_ml / 1000

# 4. Вывод результата
print()
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
