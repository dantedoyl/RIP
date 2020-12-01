from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any
from watcher import NewPizzaObserver, FinishPizzaObserver
from facade import Facade

class Pizza():

    def __init__(self) -> None:
        self.dough = []
        self.sauce = []
        self.topping = []

    def set_dough(self, part: Any) -> None:
        self.dough.append(part)
    def set_sauce(self, part: Any) -> None:
        self.sauce.append(part)
    def set_topping(self, part: Any) -> None:
        self.topping.append(part)

    def list_parts(self) -> None:
        print(f"Dough: {', '.join(self.dough)}", end="\n")
        print(f"Sauce: {', '.join(self.sauce)}", end="\n")
        print(f"Topping: {', '.join(self.topping)}", end="\n")

class PizzaBuilder(ABC):
    pizza_type = None

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_dough(self) -> None:
        pass

    @abstractmethod
    def produce_sauce(self) -> None:
        pass

    @abstractmethod
    def produce_topping(self) -> None:
        pass


class SpicyPizzaBuilder(PizzaBuilder):

    def __init__(self) -> None:
        self.pizza_type = "Spicy Pizza"
        self.reset()

    def reset(self) -> None:
        self._product = Pizza()


    @property
    def product(self) -> Pizza:
        product = self._product
        self.reset()
        return product

    def produce_dough(self) -> None:
        self._product.set_dough("Standart")

    def produce_sauce(self) -> None:
        self._product.set_sauce("Spicy")

    def produce_topping(self) -> None:
        self._product.set_topping("Tomatoes")

class HawaiianPizzaBuilder(PizzaBuilder):

    def __init__(self) -> None:
        self.pizza_type = "Hawaiian Pizza"
        self.reset()

    def reset(self) -> None:
        self._product = Pizza()


    @property
    def product(self) -> Pizza:
        product = self._product
        self.reset()
        return product

    def produce_dough(self) -> None:
        self._product.set_dough("Fat")

    def produce_sauce(self) -> None:
        self._product.set_sauce("Katchup")

    def produce_topping(self) -> None:
        self._product.set_topping("Pineapple")


class Cook:

    def __init__(self, name, new_observer, finish_observer) -> None:
        self._builder = None
        self.name = name
        self._new_pizza_observer = new_observer or NewPizzaObserver()
        self._finish_pizza_observer = finish_observer or FinishPizzaObserver()

    @property
    def builder(self) -> PizzaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: PizzaBuilder) -> None:
        self._builder = builder
        self.notify(self._new_pizza_observer)

    def build_only_sauce_pizza(self) -> None:
        self.builder.produce_dough()
        self.builder.produce_sauce()
        self.notify(self._finish_pizza_observer)

    def build_full_pizza(self) -> None:
        self.builder.produce_dough()
        self.builder.produce_sauce()
        self.builder.produce_topping()
        self.notify(self._finish_pizza_observer)

    def notify(self, observer: PizzaObserver) -> None:
        print("Наблюдатель говорит:")
        observer.update(self)


if __name__ == "__main__":

    director1 = Cook("NewCook1", None, None)
    builder1 = SpicyPizzaBuilder()
    director1.builder = builder1

    director2 = Cook("NewCook2", None, None)
    builder2 = HawaiianPizzaBuilder()
    director2.builder = builder2

    cookers = Facade(director1, director2)
    cookers.cooke1_operation()
    cookers.cooker2_operation()
