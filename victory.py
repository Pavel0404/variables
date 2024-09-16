print('Добро пожаловать на викторину!')

correct_answers = 0
errors = 0

def check_answer(user_answer, correct_answer):
    global correct_answers, errors
    if user_answer == correct_answer:
        correct_answers += 1
    else:
        errors += 1

def calculate_percentages(correct, total):
    return (correct * 100) / total

while True:
    a1 = input('Введите год рождения группы АЛИСА: ') #1982
    a2 = input('Введите год рождения группы Metallica: ') #1981
    a3 = input('Введите год рождения группы Red Hot Chili Peppers: ') #1996
    a4 = input('Введите год рождения группы Linkin Park: ') #1994
    a5 = input('Введите год рождения группы Guano_Apes: ') #1993

    check_answer(a1, "1982")
    check_answer(a2, "1981")
    check_answer(a3, "1996")
    check_answer(a4, "1994")
    check_answer(a5, "1993")

    total_questions = 5
    correct_percentage = calculate_percentages(correct_answers, total_questions)
    incorrect_percentage = calculate_percentages(errors, total_questions)

    print('Количество правильных ответов:', correct_answers)
    print('Количество ошибок:', errors)
    print('Процент правильных ответов:', correct_percentage)
    print('Процент неправильных ответов:', incorrect_percentage)

    play_again = input('Хотите начать игру сначала? (Да/Нет): ')
    if play_again.strip().lower() != 'да':
       break
print('Всего доброго! ')