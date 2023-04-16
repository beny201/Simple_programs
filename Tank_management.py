"""1) Stwórz klasę Tank (zbiornik).
Zbiornik posiada następujące atrybuty: nazwę oraz pojemność.
Należy stworzyć następujące operacje:
-	pour_water(volume) - ale w zbiorniku nie może być więcej wody niż pojemność
-	pour_out_water(volume) - ale nie można odlać więcej wody niż jest dostępne w zbiorniku
-	transfer_water(from, volume) - przelewa wodę ze zbiornika “from” do naszego (pod warunkiem, że przelewanie jest możliwe)
Dodatkowo stworzyć metody, które pozwalają:
-	Znaleźć zbiornik, w którym jest najwięcej wody
-	Znaleźć zbiornik, który jest najbardziej zapełniony
-	Znaleźć wszystkie puste zbiorniki
2) Każda operacja na zbiorniku jest rejestrowana.
Dla każdej operacji pamiętamy: datę i czas jej wykonania, jej nazwę, zbiornik, na którym była ona wykonana oraz ilość wody, jaka była brana pod uwagę oraz to, czy operacja się powiodła czy nie.

Należy zaimplementować taką funkcjonalność oraz dodatkowo stworzyć metody, które:
-	Pozwalają znaleźć zbiornik, na którym było najwięcej operacji zakończonych niepowodzeniem
-	Pozwalają znaleźć zbiornik, w którym było najwięcej operacji danego typu (typ podajemy jako argument metody)"""

from __future__ import annotations
import datetime
from typing import List


class TankLogs:
    actions = {}


class TankManager:
    list_of_tanks: List[Tank] = []

    @staticmethod
    def add_to_actions(function):

        def wrapper(*args, **kwargs):
            method_name = function.__name__
            key = len(TankLogs.actions) + 1
            now = datetime.datetime.now()
            dt_now = now.strftime("%d/%m/%Y %H:%M:%S")
            if len(args) > 2:
                value = {"Action": method_name, "Tank": [args[0].name,
                                                         args[1].name],
                         "Volume": args[2], "Date": dt_now, "Success": None}
            else:
                value = {"Action": method_name, "Tank": args[0].name,
                         "Volume": args[1],
                         "Date": dt_now, "Success": None}

            value["Success"] = function(*args, **kwargs)
            TankLogs.actions[key] = value
            return function(*args, **kwargs)

        return wrapper

    @staticmethod
    def most_filled() -> str:
        max_filling = max(
            (tank.fill / tank.capacity if tank.fill != 0 else 0) for tank in
            TankManager.list_of_tanks)
        return \
            [tank for tank in TankManager.list_of_tanks if
             tank.fill != 0 and tank.fill / tank.capacity ==
             max_filling][0].name

    @staticmethod
    def most_liquid() -> str:
        max_filling = max(tank.fill for tank in TankManager.list_of_tanks)
        return [tank for tank in TankManager.list_of_tanks if tank.fill ==
                max_filling][0].name

    @staticmethod
    def empty_tanks() -> List[Tank]:
        return [tank for tank in TankManager.list_of_tanks if tank.fill == 0]

    @staticmethod
    def failed_task() -> None:
        counter = {}
        for values in TankLogs.actions.values():
            if not values["Success"]:
                if type(values["Tank"]) == list:
                    for tank in values["Tank"]:
                        if tank not in counter:
                            counter[tank] = 1
                        else:
                            counter[tank] += 1
                else:
                    if values["Tank"] not in counter:
                        counter[values["Tank"]] = 1
                    else:
                        counter[values["Tank"]] += 1
        print(counter)
        max_failed_tank_name, max_failed = '', 0
        for tank_name, no_of_failed_task in counter.items():
            if no_of_failed_task > max_failed:
                max_failed_tank_name = tank_name
                max_failed = no_of_failed_task
        print(max_failed_tank_name, max_failed)

    @staticmethod
    def most_used(method) -> None:
        counter_for_most_used = {}
        for values in TankLogs.actions.values():
            if values["Action"] == method:
                if type(values["Tank"]) == list:
                    for tank in values["Tank"]:
                        if tank not in counter_for_most_used:
                            counter_for_most_used[tank] = 1
                        else:
                            counter_for_most_used[tank] += 1
                else:
                    if values["Action"] not in counter_for_most_used:
                        counter_for_most_used[values["Tank"]] = 1
                    else:
                        counter_for_most_used[values["Tank"]] += 1

        print(counter_for_most_used)
        max_used_tank_name, max_used = '', 0
        for tank_name, no_of_used_tank in counter_for_most_used.items():
            if no_of_used_tank > max_used:
                max_used_tank_name = tank_name
                max_used = no_of_used_tank
        print(max_used_tank_name, max_used)


class Tank:

    def __init__(self, name: str, capacity: float, fill: float = 0) -> None:
        self.name = name
        self.capacity = capacity
        self.fill = fill
        TankManager.list_of_tanks.append(self)

    def __str__(self) -> str:
        return self.name

    def __repr__(self):
        return f"{self.name}"

    @TankManager.add_to_actions
    def pour_water(self, volume: float) -> bool:
        if volume <= self.capacity - self.fill:
            self.fill += volume
            return True
        else:
            print("Not enough capacity")
            return False

    @TankManager.add_to_actions
    def pour_out(self, volume: float) -> bool:
        if volume <= self.fill:
            self.fill -= volume
            return True
        else:
            print(f"Not enough liquid, will be used {self.fill}")
            self.fill -= self.fill
            return False

    @TankManager.add_to_actions
    def transfer_water(self, from_tank, volume: float) -> bool:
        if from_tank.fill >= volume <= (self.capacity - self.fill):
            self.fill += volume
            from_tank.fill -= volume
            print(f"Action completed: {self.fill} was transferred to"
                  f" {self.name} from {from_tank.name}")
            return True
        else:
            print(f"Action not possible. Tank from which you wanted "
                  f"transfer {from_tank.fill}, self capacity {self.capacity}")
            return False


def main():
    t1 = Tank("first tank", 1000)
    t1.pour_water(100)
    t1.pour_out(1000)
    print(t1.fill)
    t2 = Tank("second tank", 60, )
    t3 = Tank("third tank", 0, )
    t2.pour_water(20)
    print(t1.capacity)
    t2.transfer_water(t1, 10)
    print(f"Most liquid: {TankManager.most_liquid()}")
    print(f"Most filled: {TankManager.most_filled()}")
    print(f"All empty tanks")
    print(TankManager.empty_tanks())
    print("Tank with ")
    TankManager.most_used("pour_out")
    print(TankLogs.actions)
    TankManager.failed_task()


if __name__ == "__main__":
    main()
