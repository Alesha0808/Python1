from __future__ import annotations
from abc import ABC, abstractmethod
import random

class GumballMachine(ABC):
    _state = None
    count = 0

    def __init__(self, numberGumballs) -> None:
        self.set_state(NoQuarterState)
        self.count = numberGumballs

    def set_state(self, state: State):
        print(f"Переходим в сосояния: {state.toString(self)}")
        self._state = state

    def insertQuarter(self):
        self._state.insertQuarter(self)

    def ejectQuarter(self):
        self._state.ejectQuarter(self)

    def turnCrank(self):
        self._state.turnCrank(self)
        self._state.dispense(self)

    def releaseBall(self):
        print('Шарик катится к выходу')
        if self.count != 0:
            self.count = self.count - 1

    def getCount(self) -> int:
        return self.count

    def refill(self,c):
        self.cout = c
        self.set_state(NoQuarterState)

    def toString(self) -> str:
        result = '\n-----------------------------------\n'
        result = result + 'Mighty Gumball, Inc.\n'
        result = result + f'Запас: {self.count} шариков\n'
        result = result + f'Состояние: {self._state.toString(self)}'
        return  result

class State(ABC):
    _context = None

    @property
    def context(self) -> GumballMachine:
        return self._context

    @context.setter
    def context(self, context: GumballMachine) -> None:
        pass

    @abstractmethod
    def insertQuarter(self) -> None:
        pass

    @abstractmethod
    def ejectQuarter(self) -> None:
        pass

    @abstractmethod
    def turnCrank(self) -> None:
        pass

    @abstractmethod
    def dispense(self)-> None:
        pass

    @abstractmethod
    def toString(self) -> str:
        pass

class NoQuarterState(State):
    def insertQuarter(self) -> None:
        print("Вы вставили монету")
        self.set_state(HasQuarterState)

    def ejectQuarter(self) -> None:
        print("Вы не вставили монету")

    def turnCrank(self) -> None:
        print("Вы дренули рычаг, но монеты нет")

    def dispense(self) -> None:
        print("Сначала нужно заплатить")

    def toString(self) -> str:
        return 'ожидание монеты'

class SoldOutState(State):
    def insertQuarter(self) -> None:
        print("Вы не можете вставить монету, автомат пуст")

    def ejectQuarter(self) -> None:
        print("Вы не можете вставить монету, автомат пуст")

    def turnCrank(self) -> None:
        print("Вы повернули рычаг, но автомат пуск")

    def dispense(self) -> None:
        print("Автомат пуст")

    def toString(self) -> str:
        return 'Автомат пуст'

class HasQuarterState(State):
    def insertQuarter(self) -> None:
        print("Вы не вставить ещё одну монету")

    def ejectQuarter(self) -> None:
        print("Монета возвращена")
        self.set_state(HasQuarterState)

    def turnCrank(self) -> None:
        print("Вы повернули рычаг...")
        winner = random.randint(0,1)
        if winner == 0 and self.getCount() > 0:
            self.set_state(WinnerState)
        else:
            self.set_state(SoldState)

    def dispense(self) -> None:
        print("Шарик не может быть выдан")

    def toString(self) -> str:
        return 'Ожидание поворота рычага'

class SoldState(State):
    def insertQuarter(self) -> None:
        print("Подожите, вы уже получили жвачку")

    def ejectQuarter(self) -> None:
        print("Извините, вы уже дернули за рычаг")

    def turnCrank(self) -> None:
        print("Поворачивать второй раз - бессмыленно")

    def dispense(self) -> None:
        self.releaseBall()
        if self.getCount() > 0:
            self.set_state(NoQuarterState)
        else:
            print('Упс, закончились шарики!')
            self.set_state(SoldOutState)

    def toString(self) -> str:
        print("Выдан шарик")

class WinnerState(State):
    def insertQuarter(self) -> None:
        print("Подожите, вы уже получили жвачку")

    def ejectQuarter(self) -> None:
        print("Извините, вы уже дернули за рычаг")

    def turnCrank(self) -> None:
        print("Поворачивать второй раз - бессмыленно")

    def dispense(self) -> None:
        print("ВЫ ИГРАЛИ! Вы получите 2 шарика!")
        self.releaseBall()
        if self.getCount() == 0:
            self.set_state(SoldOutState)
        else:
            self.releaseBall()
            if self.getCount() > 0:
                self.set_state(NoQuarterState)
            else:
                print('Упс, закончились шарики!')
                self.set_state(SoldOutState)

    def toString(self) -> str:
        print("Получено 2 шарика, потому что Вы победитель!")

    def main():
        gumballMachine = GumballMachine(10)

        print(gumballMachine.toString())

        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()

        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()

    if __name__=="__main__":
        main()