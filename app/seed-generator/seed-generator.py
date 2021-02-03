import requests
import json

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

querystring = {"number": "2"}

headers = {
    'x-rapidapi-key': "52c0634099mshe1bd7382624fc80p16320ajsn6a322fd0e228",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
i = 0
j = 0

for recipe in data['recipes']:
    title = recipe['title']
    vegetarian = recipe['vegetarian']
    description = recipe['summary']
    time = recipe['readyInMinutes']
    cheap = recipe['cheap']
    glutenfree = recipe['glutenFree']
    pricePerServing = recipe['pricePerServing']
    servings = recipe['servings']
    # image = recipe['image']

    recipeSeed = {
        'description': description,
        'title': title,
        'vegetarian': vegetarian,
        'time': time,
        'cheap': cheap,
        'glutenfree': glutenfree,
        'pricePerServing': pricePerServing,
        'servings': servings,
        # 'image': image
    }
    # print(recipeSeed)
    j = j + 1
    for ingredient in recipe['extendedIngredients']:
        ingredientName = ingredient['originalName']
        amount = ingredient['amount']
        unit = ingredient['unit']
        print(unit)
        ingredientSeed = {
            'recipeId': j,
            'ingredientName': ingredientName,
            'amount': amount,
            'unit' : unit

        }

        print(ingredientSeed)
    
    
    
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
            # print(instructionsSeed)
