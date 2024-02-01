friends = input().split(", ")

while True:
    command = input().split()
    if command[0] == "Report":
        break
    elif command[0] == "Blacklist":
        name = command[1]
        if name in friends:
            index = friends.index(name)
            friends[index] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    elif command[0] == "Error":
        index = int(command[1])
        if 0 <= index < len(friends) and friends[index] != "Blacklisted" and friends[index] != "Lost":
            print(f"{friends[index]} was lost due to an error.")
            friends[index] = "Lost"
    elif command[0] == "Change":
        index = int(command[1])
        new_name = command[2]
        if 0 <= index < len(friends):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name

print(f"Blacklisted names: {friends.count('Blacklisted')}")
print(f"Lost names: {friends.count('Lost')}")
print(" ".join(friends))