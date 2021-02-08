import random
import json


reviewTable = []

for x in range(200):
    userId = random.randint(3, 10)
    recipeId = random.randint(1,50)
    posoverall = random.randint(3, 5)
    negoverall = random.randint(3, 5)
    positivearray = ["Never tried this type of food before", 'My family loved this!', 'I have to keep trying to master this dish!', "If you dont like this there is something wrong with you!", "I loved this", "This was great", "Awesome!", "I will always treasure this recipe", "Whoever Wrote this is a genius!", "I followed along so easily!"]
    negativearray = ("This was terrible", "Okay, it was not terrible, but really?", "Whatever")
    review = random.choice(positivearray)
    
    reviewSeed = {
                'overall': posoverall,
                'review': review,
                'recipeId': recipeId,
                'userId' : userId

            }
    reviewTable.append(reviewSeed)


with open('recipe1.json', 'w') as f:
    json.dump(reviewTable, f, indent=2)
