class BMW:
    def fuel_type(self):
        return "Diesel/Petrol/Electric"

    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "High-octane Petrol"

    def max_speed(self):
        return "340 km/h"


def car_details(car_object):
    print(f"Fuel Type: {car_object.fuel_type()}")
    print(f"Max Speed: {car_object.max_speed()}")
    print("-" * 30)


bmw_car = BMW()
ferrari_car = Ferrari()

print("BMW Details:")
car_details(bmw_car)

print("Ferrari Details:")
car_details(ferrari_car)
