n = int(input())
cars = set()

for _ in range(n):
    data = input().split(', ')
    direction, car_plate = data

    if direction == 'IN':
        cars.add(car_plate)
    elif direction == 'OUT':
        if car_plate in cars:
            cars.remove(car_plate)

if cars:
    for car in cars:
        print(car)
else:
    print('Parking Lot is Empty')