#1
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")


donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)


donald_duck.print_information()
print()
compartment_no_6.print_information()


#2
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.kilometer_counter = 0

    def set_speed(self, speed):
        self.current_speed = min(speed, self.max_speed)

    def drive(self, hours):
        distance = self.current_speed * hours
        self.kilometer_counter += distance

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)


electric_car.set_speed(150)
gasoline_car.set_speed(120)

electric_car.drive(3)
gasoline_car.drive(3)


print(f"Electric Car ({electric_car.registration_number}) - Kilometers driven: {electric_car.kilometer_counter} km")
print(f"Gasoline Car ({gasoline_car.registration_number}) - Kilometers driven: {gasoline_car.kilometer_counter} km")
