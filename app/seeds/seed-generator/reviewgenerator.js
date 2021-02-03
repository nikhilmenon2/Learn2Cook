import random
import json


reviewTable = []

for x in range(200):
    userId = random.randint(1, 10)
    recipeId = random.randint(1, 50)
    overall = random.randint(1, 5)
    array = ["Never tried this type of food before", 'My family loved this!', 'I have to keep trying to master this dish!', "If you dont like this there is something wrong with you!", "I loved this", "This wasnt that great", "I had trouble following along, and I was totally lost", "Meh", "I will always treasure this recipe", "Whoever Wrote this is a genius!", "I cant stand this dish!", "I followed along so easily!"]
    review = random.choice(array)
    
    reviewSeed = {
                'overall': overall,
                'review': review,
                'recipeId': recipeId,
                'userId' : userId

            }
    reviewTable.append(reviewSeed)


with open('reviewTableSeeder.json', 'w') as f:
    json.dump(reviewTable, f, indent=2)
