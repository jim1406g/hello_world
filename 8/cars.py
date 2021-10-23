# import make_car as mkcar
from make_car import make_car

cars = []
cars.append(make_car('vesta', color='black'))
cars.append(make_car('kalina'))
cars.append(make_car('gazel', year='2003'))
cars.append(make_car('gazel next'))

for car in cars:
    print(f"- {car}")