from loguru import logger
from get_name_with_help_id import get_name_with_help_id
import numpy as np

country = {}

logger.remove()
logger.add(
        sink='logs/find_part.log',
        level='INFO',
        mode='w',
        format='{time:H:mm:ss} | <level>{level}</level> | {line}: {message}',
)


def find_part_focus(file: str) -> dict:
    name_country = file[file.rfind('/') + 1:file.find('.')]
    tag = get_name_with_help_id(name_country)
    number_of_spaces_focus = None
    focuses = {}
    print(f'{name_country.capitalize()}: {tag}')
    with open(file, 'r', encoding='UTF-8') as focus_file:
        focus_block = False
        prerequisite = None
        prerequisite_block = False
        mutually_exclusive_block = False
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
                                    ' focus = '
                            )
                            focus_dict['prerequisite'] = prerequisite
                            prerequisite = ', '.join(i.strip() for i in prerequisite)

                    if line.startswith('mutually_exclusive =') or mutually_exclusive_block != False:
                        focus_count = line.count('focus =')
                        if mutually_exclusive_block is False:
                            if focus_count == 1:
                                mutually_exclusive = line[len('mutually_exclusive = { focus = '):line.rfind('}') - 1]
                                focus_dict['mutually_exclusive'] = mutually_exclusive
                            elif focus_count == 0:
                                mutually_exclusive_block = number_of_spaces
                            else:
                                mutually_exclusive = line[
                                                     len('mutually_exclusive = { focus = '):line.rfind('}') - 1].split(
                                        ' focus = '
                                )
                                focus_dict['mutually_exclusive'] = mutually_exclusive
                                logger.info(f'Простой случай: {mutually_exclusive}')
                                mutually_exclusive = ', '.join(i.strip() for i in mutually_exclusive)
                        else:
                            if line.startswith('}'):
                                mutually_exclusive_block = False
                            else:
                                mutually_exclusive = line[len('focus = '):]
                                if focus_dict.get('mutually_exclusive') != None:
                                    if isinstance(focus_dict.get('mutually_exclusive'), list):
                                        mutually_exclusive1 = focus_dict.get('mutually_exclusive')
                                        all_mutually_exclusive = mutually_exclusive1.append(mutually_exclusive)
                                    else:
                                        mutually_exclusive1 = focus_dict.get('mutually_exclusive')
                                        all_mutually_exclusive = [mutually_exclusive, mutually_exclusive1]
                                        focus_dict['mutually_exclusive'] = all_mutually_exclusive
                                    logger.info(f'{all_mutually_exclusive}')
                                else:
                                    focus_dict['mutually_exclusive'] = mutually_exclusive
                                    logger.info(mutually_exclusive)

                    if line.startswith('cost ='):
                        if focus_dict.get('cost') is None:
                            cost = line[len('cost = '):]
                            focus_dict['cost'] = cost

                    if line.startswith('}') and number_of_spaces == number_of_spaces_focus:
                        logger.info(f'ID: {id_focus}, cost: {cost}, prerequisite: {prerequisite}')
                        focus_block = False
                        if focus_dict.get('prerequisite') is None:
                            focus_dict['prerequisite'] = 'None'
                        if focus_dict.get('mutually_exclusive') is None:
                            focus_dict['mutually_exclusive'] = 'None'
                        logger.info(id_focus)
                        focuses[id_focus] = focus_dict.copy()
                        logger.info(f'{id_focus}\n')
                        country[tag] = focuses
                        focus_dict.clear()
                        number_of_spaces_focus = None
