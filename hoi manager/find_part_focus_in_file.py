from loguru import logger
from get_name_with_help_id import get_name_with_help_id

country = {}

logger.remove()
logger.add(
    sink='logs/find_part.log',
    level='INFO',
    mode='w',
    format='{time:H:mm:ss} | <level>{level}</level> | {line}: {message}',
)

def find_part_focus(file: str) -> dict:
    name_country = file[file.rfind('/')+1:file.find('.')]
    tag = get_name_with_help_id(name_country)
    number_of_spaces_focus = None
    focuses = {}
    print(f'{name_country.capitalize()}: {tag}')
    with open(file, 'r', encoding='UTF-8') as focus_file:
        focus_block = False
        prerequisite = None
        focus_dict = {}
        for line in focus_file.readlines():
            number_of_spaces = line.count('\t')
            line = line.strip()
            if line.startswith('focus = {') or focus_block is True:
                if number_of_spaces_focus is None:
                    number_of_spaces_focus = number_of_spaces
                line = line.replace('#', '')
                focus_block = True
                if focus_block:
                    if line.startswith('id ='):
                        if focus_dict.get('id') is None:
                            id_focus = line[len('id = '):]
                            logger.info(f'ID фокуса: {id_focus}')
                            focus_dict['id'] = id_focus
                    if line.startswith('prerequisite ='):
                        focus_count = line.count('focus =')
                        if focus_count == 1:
                            prerequisite = line[len('prerequisite = { focus = '):line.rfind('}') - 1]
                            focus_dict['prerequisite'] = prerequisite
                        else:
                            prerequisite = line[len('prerequisite = { focus = '):line.rfind('}') - 1].split(
                                ' focus = ')
                            focus_dict['prerequisite'] = prerequisite
                            prerequisite = ', '.join(i.strip() for i in prerequisite)

                    if line.startswith('prerequisite ='):
                        focus_count = line.count('focus =')
                        if focus_count == 1:
                            prerequisite = line[len('prerequisite = { focus = '):line.rfind('}') - 1]
                            focus_dict['prerequisite'] = prerequisite
                        else:
                            prerequisite = line[len('prerequisite = { focus = '):line.rfind('}') - 1].split(
                                ' focus = ')
                            focus_dict['prerequisite'] = prerequisite
                            prerequisite = ', '.join(i.strip() for i in prerequisite)

                    if line.startswith('cost ='):
                        if focus_dict.get('cost') is None:
                            cost = line[len('cost = '):]
                            focus_dict['cost'] = cost

                    if line.startswith('}') and number_of_spaces == number_of_spaces_focus:
                        logger.info(f'ID: {id_focus}, cost: {cost}, prerequisite: {prerequisite}')
                        focus_block = False
                        if focus_dict.get('prerequisite') is None:
                            focus_dict['prerequisite'] = 'None'
                        logger.info(id_focus)
                        focuses[id_focus] = focus_dict.copy()
                        logger.info(f'{id_focus}\n')
                        country[tag] = focuses
                        focus_dict.clear()
                        number_of_spaces_focus = None