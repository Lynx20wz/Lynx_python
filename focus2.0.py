import re
import sys
focus_name_massiv = []
focus_dictionary = {}

class focus_class:
    #инициализация
    def __init__(self, id, cost, prerequisite=None, mutually_exclusive=None, create_focus=None):
        self.id = id
        self.cost = cost
        self.prerequisite = prerequisite
        self.mutually_exclusive = mutually_exclusive
        focus_name_massiv.append(self.id)
        focus_dictionary[id] = {'self': self, 'id': self.id, 'cost': self.cost, 'prerequisite': self.prerequisite, 'mutually_exclusive': self.mutually_exclusive}
        if create_focus == 1:
            self.focus_to_file(id, cost, prerequisite, mutually_exclusive)
        else:
            ...

    def info(self):
        output = f'\nФокус: "{self.id}" | {self.cost}\n'
        if self.prerequisite:
            output += f'prerequisite: {self.pre}\n'
        if self.mutually_exclusive:
            output += f'mutually_exclusive: {self.muex}\n'
        return output
    
    @staticmethod
    def all_focus():
        output = ', '.join(focus_name_massiv)
        return output
    
    def clear_focus_file():  #очитска всего файла
        focus_name_massiv.clear()
        with open("focus.txt", "w") as file:
            file.write('')
        print("Содержимое файла focus.txt было полностью удалено.")

    def search_focus_in_dictionary(id):
        for search_focus in focus_dictionary:
            if search_focus == id:
                search_focus = focus_dictionary[search_focus]['self']
                return search_focus
    
    
    #блок изменений частей
    def set_id(self, id):
        self.id = id

    def set_cost(self, cost):
        self.cost = cost

    def set_pre(self, prerequisite):
        self.pre = prerequisite

    def set_muex(self, mutually_exclusive):
        self.muex = mutually_exclusive

    def editing_focus(self):
        ...

    def focus_to_file(self, id, cost, prerequisite=None, mutually_exclusive=None):
        with open("focus.txt", 'a') as focus_file:
            focus_entry = f"focus = {{\n    id = {self.id}\n    cost = {self.cost}\n"
            focus_entry += f'}}\n\n'
            focus_file.write(focus_entry)


print("Задрвствуйте, это программа создана для моддинга в Heart of Iron4. В данный момент вам доступны следующие комнады: \nНастройки, фокусы, выход")

#считывание созданных фокусов в файле
try:
    with open("focus.txt", 'r') as focus_file:
        for line in focus_file:
            if "focus = {" in line:
                focus_block = True
                while focus_block:
                    for line in focus_file:
                        if "id = " in line:
                            find_id = line[line.find("id = ") + len("id = "):].strip()
                        if "cost = " in line:
                            find_cost = line[line.find("cost = ") + len("cost = "):].strip()
                        if "prerequisite =" in line:
                            find_prerequisite = line[line.find("prerequisite = ") + len("prerequisite = "):].strip()
                        else: 
                            find_prerequisite = None
                        if "mutually_exclusive =" in line:
                            find_mutually_exclusive = line[line.find("mutually_exclusive = ") + len("mutually_exclusive = "):].strip()
                        else: 
                            find_mutually_exclusive = None
                        if "}" in line:
                            focus_block = False
                            find_id = focus_class(find_id, find_cost, find_prerequisite, find_mutually_exclusive)

except FileNotFoundError:
    print("Файл с фокусами не был найден!")
    not_file = True

if len(focus_name_massiv) > 0:
    print(f"Всего было найдено фокусов {len(focus_name_massiv)}:")
    #print(', '.join(focus_name_massiv))
    print(focus_class.all_focus())

else:
    print("Фокусы в файле не найдены!")

while True:
    command = input("Введите команду: ").lower()
    if command == 'focus' or command == 'фокусы':
        while True:
            #Обновление перемнных
            id = ''
            cost = ''

            id = input("Введите название фокуса: ")
            if re.match(r'^[a-zA-Z0-9_ ]+$', id):
                if id in focus_name_massiv:
                    quest_repeat_focus = input("Что сделать с фокусом?\nИзменить, просмотреть: ").lower()
                    if quest_repeat_focus == 'edit' or quest_repeat_focus == 'изменить':
                        id.editing_focus()
                    if quest_repeat_focus == 'look' or quest_repeat_focus == 'просмотреть':
                        id_focus_class = focus_class.search_focus_in_dictionary(id)
                        print(id_focus_class.info())
                        
                else:
                    cost = input("Сколько недель будет проходиться фокус? ")
                    if cost == 'back' or cost == 'назад':
                        break
                    else:
                        id_focus_class = (focus_class(id, cost, create_focus=1))
                        print(f'Фокус {id} был создан!:\n{id_focus_class.info()}')
            
    else:
        print("Команда не найдена, повторите попытку")
