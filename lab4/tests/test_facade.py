import unittest
from facade import Facade
from pizzabuilder import Cook

test_cooker1 = Cook("TestCook1", None, None)
test_cooker2 = Cook("TestCook2", None, None)


class TestFacade(unittest.TestCase):
    def test_facade_create_cooker(self):
        facade = Facade(test_cooker1, test_cooker2)
        unknown_cooker1 = facade.cooker1
        unknown_cooker2 = facade.cooker2

        self.assertEqual(unknown_cooker1.name, test_cooker1.name)

        self.assertEqual(unknown_cooker2.name, test_cooker2.name)

if __name__ == '__main__':
    unittest.main()