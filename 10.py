#1,2,3:

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Target floor is out of range.")
            return

        print(f"Moving to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"{elevator_number} to floor {target_floor}")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Invalid.")

    def fire_alarm(self):
        print("Fire alarm!.")
        for i, elevator in enumerate(self.elevators):
            print(f"Moving elevator {i} to the bottom floor.")
            elevator.go_to_floor(self.bottom_floor)


building = Building(1, 10, 3)


building.run_elevator(0, 5)
building.run_elevator(1, 7)
building.run_elevator(2, 3)

building.fire_alarm()

#4
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(f"{car.registration_number}  {car.max_speed}  {car.current_speed}  {car.travelled_distance}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)
cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

race = Race("Grand Demolition Derby", 8000, cars)

hours_passed = 0
while not race.race_finished():
    race.hour_passes()
    hours_passed += 1
    if hours_passed % 10 == 0:
        print(f"Race Status after {hours_passed} hours")
        race.print_status()


print(f"Final{hours_passed} hours")
race.print_status()

