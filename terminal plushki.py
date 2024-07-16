import time
from tqdm import trange, tqdm
from colorama import *

number = int(input("Введите число: "))
for i in trange(number, colour='blue'):
    pass

time.sleep(0.01)
print('\n' + Fore.BLUE + "Установлено!")