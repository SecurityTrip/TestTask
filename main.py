import random

from Classes import Floor, SmallElevator, BigElevator

floors = []
for i in range(1, 21):
    floors.append(Floor(i))

BE = BigElevator()
SE = SmallElevator()


def simulation():
    floors[0].CallElevator()
    tmp = random.randrange(1, 2, 1)
    if tmp == 1:
        SE.pressButtonFloor(14)
    else:
        BE.pressButtonFloor(14)

    print(f"Большой лифт на {BE.CurretFloor} этаже")
    print(f"Маленький лифт на {SE.CurretFloor} этаже")

    floors[14].CallElevator()

    if BE.CurretFloor == 15:
        BE.pressButtonFloor(1)
    if SE.CurretFloor == 15:
        SE.pressButtonFloor(1)


if __name__ == "__main__":
    simulation()