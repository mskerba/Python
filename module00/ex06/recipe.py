import sys

cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def add_a_recipe():
    recipe = {}
    name = input(">>> Enter a name: ")
    print(">>> Enter ingredients: ")
    l = []
    for line in sys.stdin:
        line = line[:-1]
        if len(line):
            l.append(line)
        else:
            break
    recipe['ingredients'] = l
    recipe['meal'] = input(">>> Enter a meal type: ")
    recipe['prep_time'] = input(">>> Enter a preparation time: ")
    cookbook[name] = recipe

def delete_a_recipe():
    print("Please enter a recipe name to delete:")
    key = input(">> ")
    if key in cookbook:
        del cookbook[key]
        print("the recipe {} is delete.\n".format(key))
    else :
        print("Sorry, this recipe does not exist.\n")

def print_recipe_name():
    print("Please enter a recipe name to get its details:")
    key = input(">> ")
    if key not in cookbook:
        print("Sorry, this recipe does not exist.\n")
        return 
    recipe = cookbook[key]
    print("\nRecipe for {}:".format(key))
    print("Ingredients list: {}".format(recipe['ingredients']))
    print("To be eaten for {}.".format(recipe['meal']))
    print("Takes {} minutes of cooking.\n".format(recipe['prep_time']))


def print_cookbook():
    l = cookbook.keys()
    
    for element in l:
        print(element)
    print('\n')


def quit():
    print("Cookbook closed. Goodbye !")
    exit(0)

def print_menu():
    print("List of available option:")
    print("  1: Add a recipe")
    print("  2: Delete a recipe")
    print("  3: Print a recipe")
    print("  4: Print the cookbook")
    print("  5: Quit\n")

if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    print_menu()
    while True:
        print("Please select an option:")
        inp = input(">> ")
        if inp.isdigit() == 0:
            print("\nSorry, this option does not exist.")
            print_menu()
        else :
            print('\n')
            num = int(inp)
            if num == 1:
                add_a_recipe()
            elif num == 2:
                delete_a_recipe()
            elif num == 3:
                print_recipe_name()
            elif num == 4:
                print_cookbook()
            elif num == 5:
                quit()
            else :
                print_menu()


