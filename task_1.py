import logging
import argparse

simple_logger = logging.getLogger('Логгер для функции devizion')
simple_logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler('file_name.log', mode='a', encoding='utf-8')
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                           datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(format)
simple_logger.addHandler(file_handler)

return_logger = logging.getLogger('Логгер для вывода')
return_logger.setLevel(logging.INFO)
file_handler_2 = logging.FileHandler('result.log', mode='a',encoding='utf-8')
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                           datefmt='%Y-%m-%d %H:%M:%S')
file_handler_2.setFormatter(format)
return_logger.addHandler(file_handler_2)

def devizion(num_1: float, num_2: float):
    try:
        result = num_1 / num_2
        return_logger.info(f'Попытка деления {num_1} на {num_2} дала результат {result}')
        return result
    except ZeroDivisionError as e:
        simple_logger.error(f'Попытка деления {num_1} на {num_2}')
        return None


parser = argparse.ArgumentParser()
parser.add_argument('num1', type=float)
parser.add_argument('num2', type=float)
args = parser.parse_args()

result = devizion(args.num1, args.num2)
if result is not None:
    print(f'Результат деления: {result}')
else:
    print('Произошла ошибка при делении.')
