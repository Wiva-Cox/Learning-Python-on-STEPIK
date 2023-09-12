'''

Эта программа вычисляет индекс массы тела по входным параметрам ВЕС, РОСТ, ВОЗРАСТ
и возвращает индекс и комментарий

'''

name = input("Ведите имя: ")

print("Привет {}, сейчас посчитаем твой индекс массы тела!".format(name))

age = int(input("Сколько вам полных лет? "))
weight = float(input("Введите ваш вес в килограммах: "))
height = float(input("Введите ваш рост в метрах: "))


if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    print("Ошибочные входные данные")
else:
    bmi = round(weight / (height * height), 2)
    if age < 45:
        if bmi < 18.50:
            discription = "недостаточной массой тела"
        elif bmi < 25:
            discription = "нормальной массой тела"
        elif bmi < 30:
            discription = "избыточной массой тела"
        else:
            discription = "ожирением"
    else:
        if bmi < 22:
            discription = "недостаточной массой тела"
        elif bmi < 27:
            discription = "нормальной массой тела"
        elif bmi < 32:
            discription = "избыточной массой тела"
        else:
            discription = "ожирением"

    print("{}, ваш индекс массы тела составляет {}".format(name, bmi))

    print("Вы относитесь к группе людей с {}.".format(discription))
