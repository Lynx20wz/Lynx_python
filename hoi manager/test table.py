from prettytable import PrettyTable
from texttable import Texttable

focus = {
    'AUS_polit': {'id': 'AUS_polit', 'cost': '10', 'prerequisite': 'AUS_com'},
    'AUS_fasch': {'id': 'AUS_fasch', 'cost': '10', 'prerequisite': ['AUS_jam', 'AUS_key']},
    'AUS_start': {'id': 'AUS_start', 'cost': '10', 'prerequisite': 'None'},
}

# table_pretty = PrettyTable(field_names=['ID', 'cost', 'prerequisite'], )
table = Texttable()
table.header(['ID', 'cost', 'prerequisite'])
table.set_deco(Texttable.VLINES)

for key, value in focus.items():
    table.add_row(
            [value.get('id'), value.get('cost'),
             ', '.join(value.get('prerequisite')) if isinstance(value.get('prerequisite'), list) else value.get(
                     'prerequisite'
             )]
    )

print(table.draw())
