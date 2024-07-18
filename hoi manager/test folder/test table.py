from prettytable import PrettyTable
focus = {
    'AUS_polit': {'id': 'AUS_polit', 'cost': '10', 'prerequisite': 'AUS_com'},
    'AUS_fasch': {'id': 'AUS_fasch', 'cost': '10', 'prerequisite': ['AUS_jam', 'AUS_key']},
    'AUS_start': {'id': 'AUS_start', 'cost': '10', 'prerequisite': 'None'},
}

table = PrettyTable(field_names=['ID', 'cost', 'prerequisite'])

for key, value in focus.items():
    table.add_row([value.get('id'), value.get('cost'), ', '.join(value.get('prerequisite')) if isinstance(value.get('prerequisite'), list) else value.get('prerequisite')])

print(table)