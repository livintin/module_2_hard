import random
number = list(range(3, 21))
para = list(range(1, 21))
final = []
n = random.choice(number)
print(f'Число из первой вставки: {n}')
for i in para:
    for j in para:
        if n % (i + j) == 0:
            final.append(f'{i}{j}')
unique_pairs = set()
filtered_list = []
for number in final:
    pair = tuple(sorted(str(number)))
    if pair not in unique_pairs:
        unique_pairs.add(pair)
        filtered_list.append(number)
print(f'Пароль:', *filtered_list)

