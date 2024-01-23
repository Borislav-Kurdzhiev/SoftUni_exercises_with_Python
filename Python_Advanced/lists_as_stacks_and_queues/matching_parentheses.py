expression = input()
paren_index = []

for index in range(len(expression)):
    if expression[index] == '(':
        paren_index.append(index)
    elif expression[index] == ')':
        start_index = paren_index.pop()
        end_index = index + 1
        print(expression[start_index:end_index])