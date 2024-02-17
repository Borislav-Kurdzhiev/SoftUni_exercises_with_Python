def cookbook(*elements):
    data = {}
    result = ""

    for arg in elements:
        recipe, cuisine, ingredients = arg

        if cuisine not in data:
            data[cuisine] = {}
        data[cuisine][recipe] = ingredients

    sorted_data = sorted(data.items(), key=lambda item: (-len(item[1]), item))

    for k, v in sorted_data:
        result += f"{k} cuisine contains {len(v)} recipes:\n"
        for recipe, ingredients in sorted(v.items()):
            result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"

    return result


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))

