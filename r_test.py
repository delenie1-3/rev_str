import unittest
from revers import Reversed

class TestReversed(unittest.TestCase):
    def setUp(self):#создание экземпляра каласса при каждом запуске теста
        self.revers = Reversed()

    def test_reversed(self):
        self.assertEqual(self.revers.reversed('Qwerty !'), '! ytrewQ')#проверяю ожидаемое значение

if __name__ == '__main__':#запуск тестирования
    unittest.main()