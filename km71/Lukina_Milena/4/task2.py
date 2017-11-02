number = int(input('Введите число: '))
if number > 0:
    answer = ('sign(%s)=1' %number)
elif number <0:
    answer = ('sign(%s)=-1' % number)
else:
    answer = ('sign(%s)=0' % number)
print(answer)
