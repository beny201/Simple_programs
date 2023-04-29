"""Napisz program, który będzie wyświetlał Menu z następującymi opcjami:

1.	Dodaj notatkę
2.	Dodaj wizytówkę (Card)
3.	Wyświetl wszystkie notatki
4.	Wyświetl wszystkie wizytówki
5.	Wyjdź
"""

from typing import Tuple


class Manager:
    def __init__(self) -> None:
        self.working = True
        self.menu = Menu()
        self.note = NotesSubManager()
        self.card = CardSubManager()

        self.action = {
            1: self.note.append_note,
            2: self.card.append_card,
            3: self.note.show,
            4: self.card.show,
            5: self.finish
        }

    def start(self) -> None:
        while self.working:
            self.show_menu()
            choice = self.menu.get_choice()
            self.execute(choice)

    def finish(self) -> None:
        self.working = False

    def show_menu(self) -> None:
        self.menu.show()

    def execute(self, choice) -> None:
        if choice in self.action.keys():
            return self.action.get(choice)()
        else:
            print(f"Number out of scope choose from 1-{len(self.action.keys())}")


class Menu:
    def __init__(self) -> None:
        self.actions = {
            1: "Add notes",
            2: "Add cards",
            3: "Show all notes",
            4: "Show all cards",
            5: "Exit"
        }

    def show(self) -> None:
        print("-" * 40)
        for key, value in self.actions.items():
            print(f"{key}.{value}")
        print("-" * 40)

    @staticmethod
    def get_choice() -> int:
        choice = input("Write what you want to do: ")
        return int(choice)


class Notes:
    def __init__(self, note: str):
        self.note = note

    def __str__(self):
        return self.note


class Card:
    def __init__(self, name: str, no: str) -> None:
        self.name = name
        self.no = no

    def __str__(self):
        return f"Name {self.name}, Number: {self.no}"


class NotesSubManager:
    def __init__(self):
        self.notes = []

    @staticmethod
    def get_note() -> str:
        note = input("Write down note: ")
        return note

    def append_note(self) -> None:
        note = self.get_note()
        self.notes.append(Notes(note))

    def show(self) -> None:
        for note in self.notes:
            print(note)


class CardSubManager:
    def __init__(self):
        self.card = []

    @staticmethod
    def get_card() -> tuple[str, str]:
        name = input("Write down name: ")
        no = input("Write down number: ")
        return name, no

    def append_card(self) -> None:
        name, no = self.get_card()
        self.card.append(Card(name, no))

    def show(self) -> None:
        if len(self.card) > 0:
            for card in self.card:
                print(card)
        else:
            print("Empty list")


def main():
    manager = Manager()
    manager.start()


if __name__ == "__main__":
    main()
