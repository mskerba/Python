from book import Book
from recipe import Recipe

book = Book("My Cookbook")

# Adding recipes
recipe1 = Recipe("Salad", "starter")
recipe2 = Recipe("Pasta", "lunch")
book.add_recipe(recipe1)
book.add_recipe(recipe2)

# Retrieving recipes by name
print("Recipe by name:")
recipe = book.get_recipe_by_name("Salad")
print(recipe.name, recipe.recipe_type)

# Retrieving recipes by type
print("Recipes by type:")
recipes = book.get_recipes_by_types("lunch")
print(recipes)

# Updating a recipe
recipe1.recipe_type = "dessert"
book.add_recipe(recipe1)

# Retrieving updated recipe by type
print("Recipes by type:")
recipes = book.get_recipes_by_types("dessert")
print(recipes)

# Checking last update time
print("Last update time:", book.last_update)
