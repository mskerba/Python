
recipe_list = ["starter", "lunch", "dessert"]

class Recipe:
    description = ""
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        if cooking_lvl in range(1, 5):
            self.cooking_lvl = cooking_lvl
        if cooking_time > 0:
            self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        if recipe_type not in recipe_list:
            self.recipe_type = recipe_type

    def __str__(self):
        txt = "{} {} {} {} {} {}".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
        return txt