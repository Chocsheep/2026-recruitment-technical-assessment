from dataclasses import dataclass
from typing import List, Dict, Union
from flask import Flask, request, jsonify
import re
import string

# ==== Type Definitions, feel free to add or modify ===========================
@dataclass
class CookbookEntry:
	name: str

@dataclass
class RequiredItem():
	name: str
	quantity: int

@dataclass
class Recipe(CookbookEntry):
	required_items: List[RequiredItem]

@dataclass
class Ingredient(CookbookEntry):
	cook_time: int


# =============================================================================
# ==== HTTP Endpoint Stubs ====================================================
# =============================================================================
app = Flask(__name__)

# Store your recipes here!
cookbook = None

# Task 1 helper (don't touch)
@app.route("/parse", methods=['POST'])
def parse():
	data = request.get_json()
	recipe_name = data.get('input', '')
	parsed_name = parse_handwriting(recipe_name)
	if parsed_name is None:
		return 'Invalid recipe name', 400
	return jsonify({'msg': parsed_name}), 200

# [TASK 1] ====================================================================
# Takes in a recipeName and returns it in a form that 
def parse_handwriting(recipeName: str) -> Union[str | None]:
	letters = list(string.ascii_letters)
	letters.append(" ") # initialising list of "allowed" letters

	recipe = list(recipeName) # converting recipeName into a list for easier character manipulation 


	for i in recipe: # for each character, turn "_" and "-" into whitespace, else turn them into empty string (will be removed at end)
		if i == "_" or i == "-":
			recipe[recipe.index(i)] = " "
		elif i not in letters:
			recipe[recipe.index(i)] = ""

	for i in range(len(recipe)): # if there is a whitespace next to an existing whitespace, remove it
		if recipe[i] == " " and i < len(recipe):
			if recipe[i + 1] == " ":
				recipe[i] = ""

	for i in range(len(recipe)): # convert all characters to lowercase
		recipe[i] = recipe[i].lower()

	for i in range(len(recipe)): # capitalise any letter after a whitespace (new word)
		if recipe[i] == " ":
			recipe[i+1] = recipe[i+1].capitalize()

	if len(recipe) == 0: # if there are no remaining characters, return None
		return None

	recipe[0] = recipe[0].capitalize() # capitalise the first letter



	ans = ""

	for i in recipe: # reconstruct list into string
		ans += i

	recipeName = ans

	return recipeName # return string


# [TASK 2] ====================================================================
# Endpoint that adds a CookbookEntry to your magical cookbook
@app.route('/entry', methods=['POST'])
def create_entry():
	# TODO: implement me
	return 'not implemented', 500


# [TASK 3] ====================================================================
# Endpoint that returns a summary of a recipe that corresponds to a query name
@app.route('/summary', methods=['GET'])
def summary():
	# TODO: implement me
	return 'not implemented', 500


# =============================================================================
# ==== DO NOT TOUCH ===========================================================
# =============================================================================

if __name__ == '__main__':
	app.run(debug=True, port=8080)
