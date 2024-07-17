from rich.table import Table
from rich.console import Console
import colorama
# part_focus_m = ['id', 'cost', 'prerequisite', 'mutually_exclusive']

# class fc:
#     def __init__(self, id, cost, id_pre = None, id_muex = None):
#         self.id = id
#         self.cost = cost
#         self.pre = id_pre
#         self.muex = id_muex
#     def set_pre(self, id_pre):
#         self.pre = id_pre
#
# SOV_polit = fc(id = input("Введите id: "), cost = input("Введите cost: "))
# print(SOV_polit.id)
# print(type(SOV_polit))
# SOV_polit.pre = id_pre=(input("Введите prerequisite: "))
# print(SOV_polit, SOV_polit.id, SOV_polit.cost, SOV_polit.pre)
# new_id = input("Введите новый prerequisite: ")
# SOV_polit.set_pre(new_id)
# print(SOV_polit, SOV_polit.id, SOV_polit.cost, SOV_polit.pre)
prerequisite = []
console = Console()
print(f'\u001b[31m привет')
input()
table = Table('focus')
table.add_row(f'prerequisite {prerequisite}')
console.print(table)