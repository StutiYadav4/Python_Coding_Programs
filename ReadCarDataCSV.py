class Car:
    def __init__(self, make, fuel_type, aspiration, num_of_doors, body_style, drive_wheels,
                 engine_location, wheel_base, length, width, height, curb_weight, engine_type,
                 num_of_cylinders, engine_size, fuel_system, compression_ratio, horsepower,
                 peak_rpm, city_mpg, highway_mpg, price):
        self.make = make
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.body_style = body_style
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.engine_type = engine_type
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.fuel_system = fuel_system
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg
        self.price = price


file1 = open("car_data.csv", "r")
cars = []
for _, row in file1.read():
    car = Car(
        row['make'], row['fuel_type'], row['aspiration'], row['num_of_doors'], row['body_style'],
        row['drive_wheels'], row['engine_location'], row['wheel_base'], row['length'],
        row['width'], row['height'], row['curb_weight'], row['engine_type'],
        row['num_of_cylinders'], row['engine_size'], row['fuel_system'],
        row['compression_ratio'], row['horsepower'], row['peak_rpm'],
        row['city_mpg'], row['highway_mpg'], row['price']
    )
    cars.append(car)


