from app.models import db, Review


# Adds a demo location, you can add other locations here if you want

def seed_reviews():

    db.session.bulk_insert_mappings(Review,
                                    [
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 33,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 26,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 33,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 26,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 14,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This was totally great!",
                                            "recipeId": 28,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This was totally great!",
                                            "recipeId": 41,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 38,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 3,
                                            "review": "My family loved this!",
                                            "recipeId": 14,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This was totally great!",
                                            "recipeId": 23,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 1,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Awesome!",
                                            "recipeId": 33,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 49,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 22,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 44,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Awesome!",
                                            "recipeId": 31,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 16,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 1,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 3,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 5,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 7,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 38,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I followed along so easily!",
                                            "recipeId": 19,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 45,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I followed along so easily!",
                                            "recipeId": 16,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 12,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Awesome!",
                                            "recipeId": 26,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 8,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 26,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 22,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 43,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 9,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 21,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 48,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This was totally great!",
                                            "recipeId": 36,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 35,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 44,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 43,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 2,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 9,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I followed along so easily!",
                                            "recipeId": 40,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 32,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 9,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 28,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 12,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 3,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 32,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 7,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 8,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 21,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 42,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 3,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 27,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 16,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 33,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 47,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 50,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I loved this",
                                            "recipeId": 38,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 23,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 11,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 49,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I followed along so easily!",
                                            "recipeId": 29,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Awesome!",
                                            "recipeId": 13,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 36,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 30,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 24,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 19,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 30,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 22,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 28,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Awesome!",
                                            "recipeId": 47,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 13,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "This was totally great!",
                                            "recipeId": 23,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 49,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 19,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 10,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 29,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 27,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 28,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 48,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "My family loved this!",
                                            "recipeId": 41,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 2,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 36,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 33,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This was totally great!",
                                            "recipeId": 21,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 1,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "My family loved this!",
                                            "recipeId": 10,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 32,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I followed along so easily!",
                                            "recipeId": 14,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 48,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 7,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I followed along so easily!",
                                            "recipeId": 20,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Awesome!",
                                            "recipeId": 36,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 16,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 42,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 15,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 37,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 39,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I followed along so easily!",
                                            "recipeId": 28,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 7,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 15,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 24,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 23,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 5,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 19,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 32,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This was totally great!",
                                            "recipeId": 1,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 42,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 17,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 26,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 12,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 21,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 7,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 40,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 3,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 18,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Awesome!",
                                            "recipeId": 19,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I followed along so easily!",
                                            "recipeId": 25,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 3,
                                            "review": "This was totally great!",
                                            "recipeId": 38,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 4,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 2,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 14,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "My family loved this!",
                                            "recipeId": 20,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 26,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 28,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I loved this",
                                            "recipeId": 9,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 9,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "My family loved this!",
                                            "recipeId": 30,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Awesome!",
                                            "recipeId": 8,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 45,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 11,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 16,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I followed along so easily!",
                                            "recipeId": 41,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This was totally great!",
                                            "recipeId": 4,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 3,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I loved this",
                                            "recipeId": 29,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 13,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This was totally great!",
                                            "recipeId": 1,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 8,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Awesome!",
                                            "recipeId": 27,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 22,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 42,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 34,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 20,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 41,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I loved this",
                                            "recipeId": 18,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 38,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I followed along so easily!",
                                            "recipeId": 20,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Awesome!",
                                            "recipeId": 38,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 15,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I followed along so easily!",
                                            "recipeId": 28,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 39,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 20,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 43,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 25,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 31,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "This was totally great!",
                                            "recipeId": 27,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 8,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 35,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 20,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I followed along so easily!",
                                            "recipeId": 46,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 41,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 29,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 26,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 2,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 4,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 4,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 12,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "My family loved this!",
                                            "recipeId": 29,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This was totally great!",
                                            "recipeId": 39,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "My family loved this!",
                                            "recipeId": 31,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 16,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 28,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 5,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 15,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 2,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 3,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 33,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 25,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 4,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This was totally great!",
                                            "recipeId": 33,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "My family loved this!",
                                            "recipeId": 4,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 16,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 31,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I followed along so easily!",
                                            "recipeId": 23,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "This was totally great!",
                                            "recipeId": 19,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Awesome!",
                                            "recipeId": 40,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "My family loved this!",
                                            "recipeId": 16,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 3,
                                            "review": "My family loved this!",
                                            "recipeId": 2,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 5,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 24,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 30,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 35,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 25,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Awesome!",
                                            "recipeId": 5,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Awesome!",
                                            "recipeId": 18,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 35,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 32,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 32,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 29,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 24,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "My family loved this!",
                                            "recipeId": 32,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I followed along so easily!",
                                            "recipeId": 2,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I followed along so easily!",
                                            "recipeId": 6,
                                            "userId": 6
                                        }
                                    ]
                                    )
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the locations table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_reviews():
    db.session.execute('TRUNCATE reviews;')
    db.session.commit()
