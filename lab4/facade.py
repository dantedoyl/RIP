from __future__ import annotations


class Facade:

    def __init__(self, cooker1: Cook, cooker2: Cook) -> None:
        self.cooker1 = cooker1
        self.cooker2 = cooker2

    def cooke1_operation(self) -> None:

        print("Only sauce pizza: ")
        self.cooker1.build_only_sauce_pizza()

        print("\n")

        print("Full pizza: ")
        self.cooker1.build_full_pizza()

        print("\n")


    def cooker2_operation(self) -> None:
        print("Only sauce pizza: ")
        self.cooker2.build_only_sauce_pizza()

        print("\n")

        print("Full pizza: ")
        self.cooker2.build_full_pizza()

        print("\n")
