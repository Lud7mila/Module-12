"Логирование бегунов"
import unittest
from rt_with_exceptions import Runner
import logging

# лучше вызывать конструктор basicConfig до использования команд логирования (иначе не будет записи в файл)!!!
logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                        format=f"%(asctime)s | %(process)d | %(levelname)s |  %(module)s | %(funcName)s: %(lineno)d | %(message)s",
                        datefmt='%d-%b-%y %H:%M:%S')
logging.info("Log started.")

# # более гибкое логирование
# # создаем регистратор
# logger = logging.getLogger('log')
# logger.setLevel(logging.INFO)
#
# # создаем обработчик для файла и установим уровень отладки
# ch = logging.FileHandler(filename='example.log', encoding='UTF-8')
# ch.setLevel(logging.INFO)
#
# # строка формата сообщения
# strfmt = '[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] > %(message)s'
# # строка формата времени
# datefmt = '%d-%b-%y %H:%M:%S'
# # создаем форматтер
# formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)
#
# # добавляем форматтер к 'ch'
# ch.setFormatter(formatter)
# # добавляем ch в регистратор
# logger.addHandler(ch)
#
# logger.info('Logging started')

class RunnerTest(unittest.TestCase):
   def __test_method(self, method_name, name="test", speed=5):
       current_obj = Runner(name, speed)
       cur_method = getattr(Runner, method_name)
       [cur_method(current_obj) for _ in range(10)]
       return current_obj.distance

   def test_walk(self):
       try:
           self.assertEqual(self.__test_method(method_name='walk', name='runner1', speed=-5), 50)
           logging.info('"test_walk" выполнен успешно')
       except ValueError:
           logging.warning("Неверная скорость для Runner", exc_info=True)

   def test_run(self):
       try:
           self.assertEqual(self.__test_method(method_name='run', name=345, speed=-50), 100)
           logging.info('"test_run" выполнен успешно')
       except TypeError:
           logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

   def test_challenge(self):
       self.assertNotEqual(self.__test_method('run'), self.__test_method('walk'))
       logging.info('test_challenge" выполнен успешно')


if __name__ == '__main__':
    unittest.main()