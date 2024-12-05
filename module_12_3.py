"Заморозка кейсов"

import unittest
import module_12_1
import module_12_2

rtTS = unittest.TestSuite()
rtTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
rtTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rtTS)