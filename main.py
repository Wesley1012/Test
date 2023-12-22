sum = 0
tic = int(input('Введите необходимое колличество билетов:'))
voz = [int(input(f'Возраст посетителя №{i+1}:')) for i in range(tic)]

for j in range(len(voz)):
    if 18 <= voz[j] < 25:
        print(f'Стоимость билета №{j+1}: 990р')
        sum += 990
    elif voz[j] >= 25:
        print(f'Стоимость билета №{j+1}: 1390р')
        sum += 1390
    else:
        print(f'Стоимость билета №{j+1}: бесплатный')
if tic > 3:
    print('Доп. скидка 10%! Итого к оплате:', sum - ((sum // 100) * 10))
else:
    print('Итого к оплате:', sum)
input('Нажмите Enter для выхода\n')