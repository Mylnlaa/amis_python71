first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')
third_number = input('Введите третье число: ')
if first_number == second_number == third_number:
    answer = ('3')
elif first_number == second_number != third_number or first_number != second_number == third_number:
    answer = ('2')
else:
    answer = ('0')
print('Ответ:', answer)

