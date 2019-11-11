# coding=utf-8

#class
class Car():
    #Statiska attribut,instansattribut
    wheels = 4
    car_count = 0
    #Konstruktormetod
    #Alla metoder har parametern self som används för att komma åt de egna attributen
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.equipment = []

        Car.car_count += 1

    def present_car(self):
        print("Model: {m}, Price: {p}".format(m=self.model, p=self.price))
#static något som tillhör klassen, orginal, något som ska vara gemensamt för alla bilar.
    @staticmethod
    def calculate_price_reduction(aPrice):
        return int(aPrice * 0.66)

    def reduce_price(self):
        self.price = self.calculate_price_reduction(self.price)
        return "Priset för {c} är nu {p}".format(c=self.model, p=self.price)

    def add_equipment(self, new_equipment):
        self.equipment.append(new_equipment)

    def print_equipment(self):
        for eq in self.equipment:
            print("* " + eq)

    def get_price(self):
        return self.price

    def __add__(self, other):
        return self.price + other.get_price()

    def __iadd__(self, other):
        self.price += other.get_price()
        return self

#Objekt med attribut
bmw = Car("BMW", 100000)
volvo = Car("Volvo", 200000)

#volvo.add_equipment("Bluetooth")
#volvo.add_equipment("7 inch display")

#volvo.print_equipment()
print(bmw + volvo)
#print(bmw.reduce_price())
#print(bmw)
#print(volvo)
#print("Antal bilar: {antal}".format(antal=Car.car_count))
