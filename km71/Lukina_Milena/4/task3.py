first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')
third_number = input('Введите третье число: ')
min_number = first_number
if min_number > second_number:
    min_number = second_number
elif min_number > third_number:
    min_number = third_number
print('Ответ: ', min_number)
