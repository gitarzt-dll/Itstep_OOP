import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.money -= 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -+ 0.1
        self.money -= 5


    def is_alive(self):
        if self.progress <= -0.5:
            print("Cast out......")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress >= 5:
            print("Excellent!!!")
            self.alive = False


    def to_work(self):
        print("Go To Woork!")
        self.money += 3
        self.gladness -= 5

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")


        live_cude = random.randint(1,3)
        if live_cude == 1:
            self.to_study()
            self.to_work()
        elif live_cude == 2:
            self.to_sleep()
        elif live_cude == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()





pasha = Student(name = "Pasha")
for day in range (365):
    if pasha.alive == False:
        break
pasha.live(day)