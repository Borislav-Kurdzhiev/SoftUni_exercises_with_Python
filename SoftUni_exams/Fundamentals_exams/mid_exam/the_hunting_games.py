days = int(input())
players = int(input())
groups_energy = float(input())
water_per_day_for_one_person = float(input())
food_per_day_for_one_person = float(input())
energy_loss = [float(input()) for _ in range(days)]

total_water = days * players * water_per_day_for_one_person
total_food = days * players * food_per_day_for_one_person

for day in range(1, days + 1):
    energy_loss_per_day = energy_loss[day - 1]
    groups_energy -= energy_loss_per_day

    if groups_energy <= 0:
        print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')
        break
    elif day % 2 == 0:
        groups_energy += groups_energy * 0.05
        total_water -= total_water * 0.3
        continue

    elif day % 3 == 0:
        food_eaten = total_food / players
        total_food -= food_eaten
        groups_energy += groups_energy * 0.1

if groups_energy > 0:
    print(f'You are ready for the quest. You will be left with - {groups_energy:.2f} energy!')