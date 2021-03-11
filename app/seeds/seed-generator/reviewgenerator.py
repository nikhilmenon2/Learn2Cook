import random
import json


reviewTable = []

for x in range(200):
    userId = random.randint(3, 10)
    recipeId = random.randint(1,50)
    posoverall = random.randint(3, 5)
    negoverall = random.randint(3, 5)
    positivearray = ["Great Place", 'My family loved it here!', 'Hard Place To hate!', "If you dont like this there is something wrong with you!", "I loved this", "This was great", "Awesome!", "I will always treasure this place", "Whoever made this place is a genius!", "I am going to come back here next year!"]
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
