from typing import List, Union


class Animal:
    alive: List["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        victim: Union[Animal, None]
    ) -> None:
        if not isinstance(victim, Herbivore):
            return
        if victim.hidden or victim.health <= 0:
            return
        victim.health -= 50
        if victim.health <= 0:
            victim.die()
