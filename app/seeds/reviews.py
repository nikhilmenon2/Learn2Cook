from app.models import db, Review


# Adds a demo location, you can add other locations here if you want

def seed_reviews():

    db.session.bulk_insert_mappings(Review,
                                    [
                                        {
                                            "overall": 2,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 30,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Meh",
                                            "recipeId": 26,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 2,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 24,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 4,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 13,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 22,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 29,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 27,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I loved this",
                                            "recipeId": 30,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "My family loved this!",
                                            "recipeId": 32,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 25,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 40,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Meh",
                                            "recipeId": 7,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This wasnt that great",
                                            "recipeId": 11,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 3,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 41,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I followed along so easily!",
                                            "recipeId": 46,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 34,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 11,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 27,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 2,
                                            "review": "This wasnt that great",
                                            "recipeId": 42,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Meh",
                                            "recipeId": 8,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 42,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 1,
                                            "review": "Meh",
                                            "recipeId": 42,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 3,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I loved this",
                                            "recipeId": 47,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 2,
                                            "review": "This wasnt that great",
                                            "recipeId": 35,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 2,
                                            "review": "My family loved this!",
                                            "recipeId": 29,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 25,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I followed along so easily!",
                                            "recipeId": 10,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 1,
                                            "review": "This wasnt that great",
                                            "recipeId": 18,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 21,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 1,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 45,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 2,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I followed along so easily!",
                                            "recipeId": 3,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I followed along so easily!",
                                            "recipeId": 43,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Meh",
                                            "recipeId": 50,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 2,
                                            "review": "This wasnt that great",
                                            "recipeId": 43,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 2,
                                            "review": "My family loved this!",
                                            "recipeId": 43,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Meh",
                                            "recipeId": 1,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 3,
                                            "review": "My family loved this!",
                                            "recipeId": 24,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 7,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 1,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 32,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 45,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 18,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 15,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 50,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 2,
                                            "review": "This wasnt that great",
                                            "recipeId": 42,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 1,
                                            "review": "This wasnt that great",
                                            "recipeId": 47,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 4,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 1,
                                            "review": "This wasnt that great",
                                            "recipeId": 31,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 22,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 13,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 33,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I followed along so easily!",
                                            "recipeId": 31,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 2,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 40,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 2,
                                            "review": "My family loved this!",
                                            "recipeId": 28,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 18,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 3,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I followed along so easily!",
                                            "recipeId": 15,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 13,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 15,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I followed along so easily!",
                                            "recipeId": 10,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "This wasnt that great",
                                            "recipeId": 26,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 30,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 2,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 8,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 17,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 1,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 43,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 31,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 10,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 45,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 17,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Meh",
                                            "recipeId": 25,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Meh",
                                            "recipeId": 23,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 3,
                                            "review": "My family loved this!",
                                            "recipeId": 13,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 29,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 42,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 29,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 39,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 9,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 43,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 15,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 23,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 4,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 20,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Meh",
                                            "recipeId": 7,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 4,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I followed along so easily!",
                                            "recipeId": 9,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Meh",
                                            "recipeId": 9,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 1,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 40,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 28,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 1,
                                            "review": "My family loved this!",
                                            "recipeId": 19,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Meh",
                                            "recipeId": 27,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 47,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I followed along so easily!",
                                            "recipeId": 16,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 34,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 2,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 28,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "My family loved this!",
                                            "recipeId": 18,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I followed along so easily!",
                                            "recipeId": 38,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 24,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 1,
                                            "review": "Meh",
                                            "recipeId": 42,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 30,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I loved this",
                                            "recipeId": 3,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 29,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 30,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This wasnt that great",
                                            "recipeId": 4,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 7,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 35,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I followed along so easily!",
                                            "recipeId": 39,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 17,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 25,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 1,
                                            "review": "My family loved this!",
                                            "recipeId": 47,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 43,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I followed along so easily!",
                                            "recipeId": 19,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 47,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 26,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I followed along so easily!",
                                            "recipeId": 20,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This wasnt that great",
                                            "recipeId": 39,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 2,
                                            "review": "My family loved this!",
                                            "recipeId": 42,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 42,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I followed along so easily!",
                                            "recipeId": 41,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 1,
                                            "review": "Meh",
                                            "recipeId": 39,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 49,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 3,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 15,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 20,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "This wasnt that great",
                                            "recipeId": 16,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I loved this",
                                            "recipeId": 4,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 44,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I followed along so easily!",
                                            "recipeId": 4,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 44,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 2,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 7,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 33,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 36,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 46,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 45,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Meh",
                                            "recipeId": 3,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 15,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 11,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 29,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 17,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 6,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 1,
                                            "review": "Meh",
                                            "recipeId": 33,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 13,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 8,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I loved this",
                                            "recipeId": 43,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 44,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 11,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 5,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 11,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 2,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 33,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 2,
                                            "review": "My family loved this!",
                                            "recipeId": 6,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I loved this",
                                            "recipeId": 24,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 13,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 1,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 14,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 3,
                                            "review": "This wasnt that great",
                                            "recipeId": 45,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "My family loved this!",
                                            "recipeId": 43,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 46,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 1,
                                            "review": "This wasnt that great",
                                            "recipeId": 18,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 4,
                                            "review": "If you dont like this there is something wrong with you!",
                                            "recipeId": 12,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 36,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 42,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Meh",
                                            "recipeId": 2,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 8,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 31,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I followed along so easily!",
                                            "recipeId": 6,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 1,
                                            "review": "This wasnt that great",
                                            "recipeId": 9,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 1,
                                            "review": "Meh",
                                            "recipeId": 2,
                                            "userId": 9
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This wasnt that great",
                                            "recipeId": 44,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 26,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 9,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 3,
                                            "review": "My family loved this!",
                                            "recipeId": 25,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I loved this",
                                            "recipeId": 19,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "My family loved this!",
                                            "recipeId": 37,
                                            "userId": 6
                                        },
                                        {
                                            "overall": 1,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 34,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 45,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 13,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 35,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 1,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 11,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 1,
                                            "review": "This wasnt that great",
                                            "recipeId": 20,
                                            "userId": 5
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 3,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I will always treasure this recipe",
                                            "recipeId": 33,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 14,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 1,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 14,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 1,
                                            "review": "I have to keep trying to master this dish!",
                                            "recipeId": 37,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 2,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 46,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This wasnt that great",
                                            "recipeId": 29,
                                            "userId": 4
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 9,
                                            "userId": 2
                                        },
                                        {
                                            "overall": 1,
                                            "review": "Meh",
                                            "recipeId": 34,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 30,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 3,
                                            "review": "Whoever Wrote this is a genius!",
                                            "recipeId": 21,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 2,
                                            "review": "I followed along so easily!",
                                            "recipeId": 36,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 4,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 20,
                                            "userId": 10
                                        },
                                        {
                                            "overall": 3,
                                            "review": "I had trouble following along, and I was totally lost",
                                            "recipeId": 14,
                                            "userId": 1
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This wasnt that great",
                                            "recipeId": 45,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 5,
                                            "review": "I cant stand this dish!",
                                            "recipeId": 29,
                                            "userId": 8
                                        },
                                        {
                                            "overall": 4,
                                            "review": "Never tried this type of food before",
                                            "recipeId": 13,
                                            "userId": 3
                                        },
                                        {
                                            "overall": 5,
                                            "review": "Meh",
                                            "recipeId": 4,
                                            "userId": 7
                                        },
                                        {
                                            "overall": 5,
                                            "review": "This wasnt that great",
                                            "recipeId": 31,
                                            "userId": 2
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
