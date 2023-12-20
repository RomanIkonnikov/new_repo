# Счетчик баллов
count = 0
# Счетчик  правильных ответов
total_answer = 0


# Начало программы
print("Привет! Предлагаю проверить свои знания английского!")

user_name = (input("Напиши как тебя зовут, "))


print(f"Привет, {user_name.capitalize()}, начинаем тренировку!")
ready_to_go = input("Если готов начать - введи 'ready' ")

if ready_to_go == 'ready':
    print("Тогда начинаем!")
else:
    print("кажется вы не хотите играть. Очень жаль")
    exit()

print("Итак, у нас всего три вопроса. ")


# вопросы
question = [f"My name ___ {user_name.capitalize()} - ",
            "I ___ a coder - ", "I live ___ Moskow - "]
# Правильные ответы
answer = ['is', 'am', 'in']


# Вопрос 1
questions = input(question[0])
if questions == answer[0]:
    # Прибавляем баллы
    count += 10
    # Прибавляем количество правильных ответов
    total_answer += 1
    print("Ответ верный!")
else:
    print(f"Неверный ответ. Верный ответ {answer[0]}")

# Вопрос 2
questions = input(question[1])
if questions == answer[1]:
    count += 10
    total_answer += 1
    print("Ответ верный!")
else:
    print(f"Неверный ответ. Верный ответ {answer[1]}")

# Вопрос 3
questions = input(question[2])
if questions == answer[2]:
    count += 10
    total_answer += 1
    print("Ответ верный!")
else:
    print(f"Неверный ответ. Верный ответ {answer[2]}")
# Высчитываем процент правильных ответов
total = (100 / 3 * total_answer)
# Итоговый комментарий
coment = (f"""Итог: правильных ответов - {total_answer},
процентов - {total:.1f},
счет - {count} баллов""")

# Выводим результат
if count == 30:
    print("Отлично! Ты ответил на все вопросы, Твои знания выше всех похвал!")
    print(coment)
elif count == 20:
    print(
        f"Ты правильно ответил на {total_answer} вопроса. Твои знания выше среднего!")
    print(coment)
elif count == 10:
    print(
        f"Ты правильно ответил на {total_answer} вопрос. Тебе стоит позаниматься английским!")
    print(coment)
else:
    print("Чтож")
    print(coment)

