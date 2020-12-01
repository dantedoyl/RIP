from __future__ import annotations
from abc import ABC, abstractmethod
#from pizzabuilder import Cook


class PizzaObserver(ABC):

    @abstractmethod
    def update(self, subject: Cook) -> None:
        pass


class NewPizzaObserver(PizzaObserver):
    def update(self, subject: Cook) -> None:
        print(f"{subject.name} is cooking {subject.builder.pizza_type}\n")


class FinishPizzaObserver(PizzaObserver):
    def update(self, subject: Cook) -> None:
        print(f"{subject.name} закончил готовить пиццу {subject.builder.pizza_type}")
        print(f"Ингридиенты:")
        subject.builder.product.list_parts()
