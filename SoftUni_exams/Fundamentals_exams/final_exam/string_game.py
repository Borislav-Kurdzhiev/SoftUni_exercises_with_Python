input_string = input()

while True:
    command = input().split()

    if command[0] == "Done":
        break

    if command[0] == "Change":
        char, replacement = command[1], command[2]
        input_string = input_string.replace(char, replacement)
        print(input_string)
    elif command[0] == "Includes":
        substring = command[1]
        print(str(substring in input_string))
    elif command[0] == "End":
        substring = command[1]
        print(str(input_string.endswith(substring)))
    elif command[0] == "Uppercase":
        input_string = input_string.upper()
        print(input_string)
    elif command[0] == "FindIndex":
        char = command[1]
        print(str(input_string.find(char)))
    elif command[0] == "Cut":
        start_index, count = int(command[1]), int(command[2])
        print(input_string[start_index:start_index + count])
