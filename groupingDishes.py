def groupingDishes(dishes):

    hash = dict()

    for dish in dishes:
        dish_name = dish[0]
        for i, ingredient in enumerate(dish):
            if i:
                try:
                    hash[ingredient].add(dish_name)
                except:
                    hash[ingredient] = set()
                    hash[ingredient].add(dish_name)

    temp = []
    for ingredient in sorted(hash.keys()):
        entry = [ingredient]
        for dish_name in sorted(hash[ingredient]):
            entry.append(dish_name)
        if len(entry) > 2:
            temp.append(entry)

    return(temp)

if __name__ == '__main__':
    dishes= [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
             ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
             ["Quesadilla", "Chicken", "Cheese", "Sauce"],
             ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
    print(groupingDishes(dishes))
