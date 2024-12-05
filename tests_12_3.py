# Задача "Проверка на выносливость"
import runner
import unittest

#is_frozen = True

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def __test_method(self, method_name):
        current_obj = runner.Runner("test_object")
        cur_method = getattr(runner.Runner, method_name)
        [cur_method(current_obj) for _ in range(10)]
        return current_obj.distance

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_walk(self):
        self.assertEqual(self.__test_method('walk'), 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_run(self):
        self.assertEqual(self.__test_method('run'), 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_challenge(self):
        self.assertNotEqual(self.__test_method('run'), self.__test_method('walk'))



from my_runner_and_tournament import Tournament, Runner

#@unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [Runner("Усэйн", 10), Runner("Андрей", 9), Runner("Ник", 3)]

    def __begin_test(self, test_number, distance, *paticipants):
        result = Tournament(distance, *paticipants).start()
        self.assertIsNotNone(result, f"Пустой словарь результатов турнира №{test_number}")
        self.all_results[test_number] = {}
        for key, value in result.items():
            self.all_results[test_number][key] = str(value)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_start1(self):
        test_number = 1
        self.__begin_test(test_number, 90, self.runners[0], self.runners[2])
        self.assertTrue(self.all_results[test_number][1] == self.runners[0].name,
                        f"Ошибка: на первом месте должен быть {self.runners[0].name}")
        self.assertTrue(self.all_results[test_number][2] == self.runners[2].name,
                        f"Ошибка: на последнем месте должен быть {self.runners[2].name}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_start2(self):
        test_number = 2
        self.__begin_test(test_number, 90, self.runners[1], self.runners[2])
        self.assertTrue(self.all_results[test_number][1] == self.runners[1].name,
                        f"Ошибка: на первом месте должен быть {self.runners[1].name}")
        self.assertTrue(self.all_results[test_number][2] == self.runners[2].name,
                        f"Ошибка: на последнем месте должен быть {self.runners[2].name}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_start3(self):
        test_number = 3
        self.__begin_test(test_number, 90, self.runners[2], self.runners[0], self.runners[1])
        self.assertTrue(self.all_results[test_number][1] == self.runners[0].name,
                        f"Ошибка: на первом месте должен быть {self.runners[0].name}")
        self.assertTrue(self.all_results[test_number][2] == self.runners[1].name,
                        f"Ошибка: на втором месте должен быть {self.runners[1].name}")
        self.assertTrue(self.all_results[test_number][3] == self.runners[2].name,
                        f"Ошибка: на последнем месте должен быть {self.runners[2].name}")

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

if __name__ == '__main__':
    unittest.main()