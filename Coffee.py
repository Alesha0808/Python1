from __future__ import annotations
from abc import ABC, abstractmethod
import random

class CaffeineBeverage(ABC):

    def prepareRecipe(self) -> None:
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    def boilWater(self):
        print("Кипящая вода")

    def pourInCup(self):
        print("Наливая в чашку")

    def customerWantsCondiments(self):
        return self.true

class Tea(CaffeineBeverage):
    def berw(self) -> None:
        print("Завариваем чай")

    def addCondiments(self) -> None:
        print("Добавляем лимон")

    def customerWantsCondiments(self) -> bool:
        print('Хотите добавить молоко и сахар в кофе (д/н)?')
        answer = input()
        if answer.lower().startswith("д"):
            return True
        else:
            return False

class Coffee(CaffeineBeverage):

    def berw(self) -> None:
        print("Пропускаем кофе через фильтр")

    def addCondiments(self) -> None:
        print("Добавляем сахар и молоко")

    def customerWantsCondiments(self) -> bool:
        print('Хотите добавить молоко и сахар в кофе (д/н)?')
        answer = input()
        if answer.lower().startswith("д"):
            return True
        else:
            return False

    def main():
        tea = Tea(wwwwwww
        coffee = Coffee()

        print("Готовим чай...")
        tea.prepareRecipe()
        print()

        print("Готовим кофе...")
        coffee.prepareRecipe()

    if __name__=="__main__":
        main()