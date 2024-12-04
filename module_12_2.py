import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            fast_participant = self.participants[0]
            for participant in self.participants:
                participant.run()
                if participant.distance >= fast_participant.distance:
                    fast_participant = participant

            if fast_participant.distance >= self.full_distance:
                finishers[place] = fast_participant
                place += 1
                self.participants.remove(fast_participant)
        return finishers



class TournamentTest(unittest.TestCase):
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


    def test_start1(self):
        test_number = 1
        self.__begin_test(test_number, 90, self.runners[0], self.runners[2])
        self.assertTrue(self.all_results[test_number][1] == self.runners[0].name,
                        f"Ошибка: на первом месте должен быть {self.runners[0].name}")
        self.assertTrue(self.all_results[test_number][2] == self.runners[2].name,
                        f"Ошибка: на последнем месте должен быть {self.runners[2].name}")

    def test_start2(self):
        test_number = 2
        self.__begin_test(test_number, 90, self.runners[1], self.runners[2])
        self.assertTrue(self.all_results[test_number][1] == self.runners[1].name,
                        f"Ошибка: на первом месте должен быть {self.runners[1].name}")
        self.assertTrue(self.all_results[test_number][2] == self.runners[2].name,
                        f"Ошибка: на последнем месте должен быть {self.runners[2].name}")

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