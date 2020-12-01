from unittest import main
from unittest import TestCase
from unittest.mock import patch
from pizzabuilder import Cook, SpicyPizzaBuilder



class TestWatcher(TestCase):
    @patch('watcher.NewPizzaObserver')
    def test_new_pizza_watcher(self, MockObserver):
        observer = MockObserver
        cooker = Cook("Cooker", observer, None)
        builder1 = SpicyPizzaBuilder()
        cooker.builder = builder1
        observer.update.assert_called_once()

    @patch('watcher.FinishPizzaObserver')
    def test_finish_pizza_watcher(self, MockObserver):
        observer = MockObserver
        cooker = Cook("Cooker", None, observer)
        builder1 = SpicyPizzaBuilder()
        cooker.builder = builder1
        cooker.build_full_pizza()
        observer.update.assert_called_once()

if __name__ == '__main__':
    main()
