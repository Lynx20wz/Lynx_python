# import time
# import sys
from functools import lru_cache  # кэширование функций использовать декоратор @lru_cache

# from loguru import logger
#
# logger.remove()
# logger.add(
#         sink=sys.stdout,
#         level='INFO',
#         format='{line}: {message}',
# )
#
#
# def test(file):
#     # logger.info(file.tell())
#     for lines in file.readlines():
#         if 'neque.' in lines.strip():
#             return 'Всё ок'
#
#
# start_time1 = time.time()
# with open('123.txt', 'r') as file:
#     for line in file:
#         if 'odio' in line.strip():
#             # logger.info(file.tell())
#             print(test(file))
#             break
# end_time1 = time.time()
#
# result_t1 = end_time1 - start_time1
#
# logger.info(f'{result_t1} sec')
dict1 = {'name': 'максим', 'f_name': 'прокопишин'}
dict2 = {'name': 'вася', 'f_name': 'пупкин'}
dict3 = {'person1': {'name': 'максим', 'f_name': 'прокопишин'}, 'person2': {'name': 'вася', 'f_name': 'пупкин'}}
