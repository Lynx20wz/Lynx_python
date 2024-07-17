# используй is только для сравнения True, False (bool)
a = True
if a is True:
    print('a = True')
else:
    print(id(a))

# is можно использовать для чисел
a = 234
b = 234
if a is b: #True
    print(f'a = b | ({a})')
else:
    print(id(a), id(b))
# но лучше через ==
a = 345
b = 345
if a == b:
    print(f'a = b | ({a})')

# команда enumerate делает следующее
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
enumerate(seasons) #отдаёт картеж (1, 'Spring') (2, 'Summer')...
for index, value in enumerate(seasons, start=1):
    print(f'{index}: {value}')
# 1: Spring
# 2: Summer
# 3: Fall
# 4: Winter