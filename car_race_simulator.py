import random

class Car:
    winner = ""

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def race(self, distance):
        actual_speed = random.uniform(0.8 * self.speed, self.speed)
        time = distance / (actual_speed * (1000 / 3600))
        return time

def main():
    car1 = Car("Porsche", 200)
    car2 = Car("Lamborghini", 220)
    car3 = Car("Ferrari", 210)

    print("-------------------------------------------------")
    print("Welcome to the Car Racing Simulator!")
    print("-------------------------------------------------")
    print(" ")

    print("Choose a car for the race:")
    print(" ")
    print("1. Porsche (200 km/h)")
    print("2. Lamborghini (220 km/h)")
    print("3. Ferrari (210 km/h)")
    print(" ")

    choice = input("Enter the number of your chosen car --> ")
    print(" ")

    if choice == '1':
        chosen_car = car1
    elif choice == '2':
        chosen_car = car2
    elif choice == '3':
        chosen_car = car3
    else:
        print("Invalid choice.")
        return

    distance = 1000
    print("------------------------")
    print("Starting the race!")
    print("------------------------")

    time1 = car1.race(distance)
    time2 = car2.race(distance)
    time3 = car3.race(distance)

    print(f"The time for the Porsche: {time1:.2f} seconds.")
    print(" ")
    print(f"The time for the Lamborghini: {time2:.2f} seconds.")
    print(" ")
    print(f"The time for the Ferrari: {time3:.2f} seconds.")
    print(" ")

    if time1 < time2 and time1 < time3:
        Car.winner = car1.name
    elif time2 < time1 and time2 < time3:
        Car.winner = car2.name
    elif time3 < time1 and time3 < time2:
        Car.winner = car3.name
    else:
        Car.winner = "Tie"

    print(f"The winning car is: {Car.winner}!")
    print(" ")
    print("------------------------")
    print("End of the race!")
    print("------------------------")

if __name__ == "__main__":
    main()
