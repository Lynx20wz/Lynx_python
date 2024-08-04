import os
import sys
import re

from loguru import logger
from rich import print
from tkinter import *

print(
        "Здравствуйте, это программа предназначена для помощи при моддинге в Hearts of Iron IV. Эта программа может работать в нескольких режимах:\n1) Выбрать файл который будет локализован\n2) Выбрать файл и сделать из него заготовку под локализацию"
)
logger.remove()
ask_file_output = ''


def work(mode: int, zero: bool, space: bool, file: str = ''):
    if mode == 1:
        print('Откройте файл для локализации')
        # file = filedialog.askopenfilename(title='Выберете файл для локализации', filetypes=[('Файл hoi4', '*.txt')])
        file = "F:/Lynx_python/hoi manager/test folder/test_json/usa.txt"  # TODO убрать
        if file == '':
            print(f"Файл не выбран!")
            while True:
                q_exit = input('Попробовать ещё раз или выход?\n[в/п]: ')
                if q_exit == 'п':
                    break
                elif q_exit == 'в':
                    sys.exit()
                else:
                    print("[red]Некорректный ввод![/red] Повторите попытку.\n")
        else:
            logger.info('Выбран путь: ' + file)
            with open(file, 'r', encoding='UTF-8') as file_input:
                full_loc = {}
                for line in file_input:
                    if line.strip().startswith('id = '):
                        id_foc = line[len('id =  '):].strip()
                        loc_id = re.sub(r'^[A-Z]{3}_', '', id_foc).capitalize().replace('_', ' ')
                        full_loc[id_foc] = loc_id
            # ask_file_output = filedialog.asksaveasfile(
            #         'a',
            #         filetypes=[('Файл локализации', '*.yml'),
            #                    ('Текстовый файл', '*.txt')]
            # )
            ask_file_output = "F:/Lynx_python/hoi manager/test folder/test_json/тест.txt"  # TODO убрать
            with open(ask_file_output, 'w+', encoding='UTF-8') as file_output:
                lines = file_output.readlines()
                if not any(line.strip() == 'l_:' for line in lines):
                    file_output.write('l_english:\n')
                for key, value in full_loc.items():
                    text_output = f'{key}: "{value}"\n'
                    if zero == 'д':
                        text_output = f'{key}:0 "{value}"\n'
                    if space == 'д':
                        text_output = ' ' + text_output
                    file_output.write(text_output)


if __name__ == '__main__':
    while True:
        while True:
            working_mode = int(input("Выберите пожалуйста вариант работы [1/2]: "))
            if working_mode in ('1', '2'):
                break
            else:
                print("[red]Некорректный ввод![/red] Повторите попытку.\n")
        while True:
            print()
            need_zero = input(
                    "Нужно ли вставлять '0' в локализацию? Примеры: \n"
                    "Focus_example:0 \"Focus example\" \nИЛИ \nFocus_example: \"Focus example\" \n[д/н]: "
            )
            if need_zero in ('д', 'н'):
                break
            else:
                print("[red]Некорректный ввод![/red] Повторите попытку.\n")
        while True:
            print()
            need_space = input(
                    "Нужны ли пробелы в локализации? Примеры:\nl_english:\nUsa_focus: \"Usa focus\" \nИЛИ \nl_english:\n Usa_focus: \"Usa focus\" \n[д/н]: "
            )
            if need_space in ('д', 'н'):
                break
            else:
                print("[red]Некорректный ввод![/red] Повторите попытку.\n")
        work(working_mode, need_zero, need_space)
        print()
        print(
                "[green]Локализация успешно создана![/green]\nДля перехода в файл напишите напишите 'о', для повтора скрипта 'п', для выхода любое другое."
        )
        exit = input('[о, п, (другое)]: ')
        if exit == 'о':
            os.startfile(ask_file_output)
        elif exit == 'п':
            pass
        else:
            sys.exit()
