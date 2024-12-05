"Заморозка кейсов"

import unittest
import tests_12_3

rtTS = unittest.TestSuite()
rtTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
rtTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rtTS)