# Задача "Проверка на выносливость"
import runner
import unittest

class RunnerTest(unittest.TestCase):
    def __test_method(self, method_name):
        current_obj = runner.Runner("test_object")
        cur_method = getattr(runner.Runner, method_name)
        [cur_method(current_obj) for _ in range(10)]
        cur_distance = current_obj.distance
        del current_obj
        return cur_distance

    def test_walk(self):
        self.assertEqual(self.__test_method('walk'), 50)

    def test_run(self):
        self.assertEqual(self.__test_method('run'), 100)

    def test_challenge(self):
        self.assertNotEqual(self.__test_method('run'), self.__test_method('walk'))


if __name__ == '__main__':
    unittest.main()