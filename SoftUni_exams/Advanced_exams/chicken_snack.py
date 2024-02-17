amount_of_money = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]

food_counter = 0

while amount_of_money and prices:
    money = amount_of_money[-1]
    price = prices[0]

    if money == price:
        food_counter += 1
        amount_of_money.pop()
        prices.pop(0)
    elif money > price:
        food_counter += 1
        difference = money - price
        amount_of_money.pop()
        prices.pop(0)
        if amount_of_money:
            amount_of_money[-1] += difference
    elif amount_of_money:
        amount_of_money.pop()
        prices.pop(0)

if food_counter >= 4:
    print(f'Gluttony of the day! Henry ate {food_counter} foods.')
elif food_counter > 0:
    print(f'Henry ate: {food_counter} {"foods" if food_counter > 1 else "food"}.')
else:
    print('Henry remained hungry. He will try next weekend again.')

