liked_meals = {}
unliked_meals_count = 0

while True:
    command = input()
    if command == "Stop":
        break

    action, guest, meal = command.split("-")[0], command.split("-")[1], command.split("-")[2]

    if action == "Like":
        if guest not in liked_meals:
            liked_meals[guest] = []
        if meal not in liked_meals[guest]:
            liked_meals[guest].append(meal)
    elif action == "Dislike":
        if guest in liked_meals:
            if meal in liked_meals[guest]:
                liked_meals[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")
                unliked_meals_count += 1
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")

for guest, meals in liked_meals.items():
    print(f"{guest}: {', '.join(meals)}")

print(f"Unliked meals: {unliked_meals_count}")
