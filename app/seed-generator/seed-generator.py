import requests
import json

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

querystring = {"number": "50"}

headers = {
   
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
i = 0
j = 0

recipeTable = []
instructionTable=[]
ingredientTable=[]



for recipe in data['recipes']:
    title = recipe['title']
    vegetarian = recipe['vegetarian']
    description = recipe['summary']
    time = recipe['readyInMinutes']
    cheap = recipe['cheap']
    glutenfree = recipe['glutenFree']
    pricePerServing = recipe['pricePerServing']
    servings = recipe['servings']
    image = recipe['image']

    recipeSeed = {
        'description': description,
        'title': title,
        'vegetarian': vegetarian,
        'time': time,
        'cheap': cheap,
        'glutenfree': glutenfree,
        'pricePerServing': pricePerServing,
        'servings': servings,
        'image': image
    }

    recipeTable.append(recipeSeed)
    j = j + 1
    
    for ingredient in recipe['extendedIngredients']:
        ingredientName = ingredient['originalName']
        amount = ingredient['amount']
        unit = ingredient['unit']
        ingredientSeed = {
            'recipeId': j,
            'ingredientName': ingredientName,
            'amount': amount,
            'unit' : unit

        }

        instructionTable.append(ingredientSeed)
    
    
    
    for each in recipe['analyzedInstructions']:
        i = i + 1
        for step in each['steps']:
            listOrder = step['number']
            specification = step['step']

            instructionsSeed = {
                "recipeId": i,
                "listOrder": listOrder,
                "specification": specification

            }
            ingredientTable.append(instructionsSeed)


# print(recipeTable)
# print(instructionTable)
# print(ingredientTable)


with open('recipeTableSeeder.json', 'w') as f:
    json.dump(recipeTable, f, indent=2)

with open('instructionTableSeeder.json', 'w') as f:
    json.dump(instructionTable, f, indent=2)

with open('ingredientTable.json', 'w') as f:
    json.dump(ingredientTable, f, indent=2)
