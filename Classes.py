class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class SmallElevator(Singleton):  # Пассажирский лифт
    MAXWEIGHT = 400
    MAXPEOPLE = 5

    alavlable = True

    SPEED = 2  # m/s

    FLOORHEIGHT = 2.7  # meters

    CurretFloor = 1

    status = ["едет вверх", "едет вниз", "открывает двери", "закрывает двери", "стоит с открытыми дверьми",
              "вызов диспетчера"]
    CurrentStatusIndex = 4

    doorStatus = True

    def GetStatus(self):
        return self.status[self.CurrentStatusIndex]

    def pressButtonFloor(self, floor):
        None

    def pressButtonCloseDoors(self):
        doorStatus = False

    def pressButtonOpenDoors(self):
        doorStatus = True

    def pressButtonCallDispatcher(self):
        self.CurrentStatusIndex = 5
        print(self.status[self.CurrentStatusIndex])
        print("Идёт вызов диспетчера")

    def RunToFloor(self, floor):
        self.CurrentStatusIndex = 3
        print(self.status[self.CurrentStatusIndex])

        if floor > self.CurretFloor:
            self.CurrentStatusIndex = 0
            print(self.status[self.CurrentStatusIndex])
            # TODO логика поездки вверх

        if floor < self.CurretFloor:
            self.CurrentStatusIndex = 1
            print(self.status[self.CurrentStatusIndex])
            # TODO логика поездки вниз

        if floor == self.CurretFloor:
            self.CurrentStatusIndex = 2
            print(self.status[self.CurrentStatusIndex])
            print("Лифт уже на {self.CurretFloor} этаже")
            self.CurrentStatusIndex = 4
            print(self.status[self.CurrentStatusIndex])


class BigElevator(Singleton):  # Грусзовой лифт
    MAXWEIGHT = 800
    MAXPEOPLE = 10

    alavlable = True

    SPEED = 1.8  # m/s

    FLOORHEIGHT = 2.7  # meters

    CurretFloor = 1

    status = ["едет вверх", "едет вниз", "открывает двери", "закрывает двери", "стоит с открытыми дверьми",
              "вызов диспетчера"]
    CurrentStatusIndex = 4

    doorStatus = "Открыты"

    def GetStatus(self):
        return self.status[self.CurrentStatusIndex]

    def pressButtonFloor(self, floor):
        None

    def pressButtonCloseDoors(self):
        doorStatus = "Открыты"

    def pressButtonOpenDoors(self):
        doorStatus = "Закрыты"

    def pressButtonCallDispatcher(self):
        self.CurrentStatusIndex = 5
        print(self.status[self.CurrentStatusIndex])
        print("Идёт вызов диспетчера")

    def RunToFloor(self, floor):
        self.CurrentStatusIndex = 3
        print(self.status[self.CurrentStatusIndex])

        if floor > self.CurretFloor:
            self.CurrentStatusIndex = 0
            print(self.status[self.CurrentStatusIndex])
            # TODO логика поездки вверх

        if floor < self.CurretFloor:
            self.CurrentStatusIndex = 1
            print(self.status[self.CurrentStatusIndex])
            # TODO логика поездки вниз

        if floor == self.CurretFloor:
            self.CurrentStatusIndex = 2
            print(self.status[self.CurrentStatusIndex])
            print("Лифт уже на {self.CurretFloor} этаже")
            self.CurrentStatusIndex = 4
            print(self.status[self.CurrentStatusIndex])


class Floor:
    BigElevatorClass, SmallElevatorClass = BigElevator(), SmallElevator()

    THISFLOOR = 0

    def __init__(self, a):
        self.THISFLOOR = a

    BigEvevatorFloor = 1
    BigEvevatorStatus = BigElevatorClass.GetStatus()

    SmallEvevatorFloor = 1
    SmallEvevatorStatus = SmallElevatorClass.GetStatus()

    def CallElevator(self):
        None
