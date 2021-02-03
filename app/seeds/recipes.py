from app.models import db, Recipe


# Adds a demo location, you can add other locations here if you want

def seed_recipes():

    db.session.bulk_insert_mappings(Recipe,
                                    [
                                        {
                                            "description": "Alouette Sundried Tomato and Basil Bisque might be a good recipe to expand your soup recipe box. Watching your figure? This gluten free and dairy free recipe has 44 calories, 1g of protein, and 1g of fat per serving. This recipe serves 8 and costs 35 cents per serving. 83 people were impressed by this recipe. It is brought to you by Foodista. From preparation to the plate, this recipe takes roughly roughly 45 minutes. Head to the store and pick up bacon, all natural tomato soup, alouette all natural sundried tomato and basil spreadable cheese, and a few other things to make it today.",
                                            "title": "Alouette Sundried Tomato and Basil Bisque",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 34.82,
                                            "servings": 8,
                                            "image": "https://spoonacular.com/recipeImages/632250-556x370.jpg"
                                        },
                                        {
                                            "description": "If you want to add more dairy free recipes to your collection, Toasted Agnolotti (or Ravioli) might be a recipe you should try. One serving contains 965 calories, 41g of protein, and 28g of fat. For $1.95 per serving, this recipe covers 21% of your daily requirements of vitamins and minerals. This recipe serves 2. It works well as a main course. 7 people have tried and liked this recipe. If you have g pre-made agnolotti/ravioli, egg, breadcrumbs, and a few other ingredients on hand, you can make it. Not a lot of people really liked this Mediterranean dish. It is brought to you by Foodista. From preparation to the plate, this recipe takes around around 45 minutes.",
                                            "title": "Toasted Agnolotti (or Ravioli)",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 195.19,
                                            "servings": 2,
                                            "image": "https://spoonacular.com/recipeImages/631807-556x370.jpg"
                                        },
                                        {
                                            "description": "Easy Onion Cheese Rounds might be just the side dish you are searching for. For 25 cents per serving, this recipe covers 5% of your daily requirements of vitamins and minerals. This recipe serves 8. One portion of this dish contains about 3g of protein, 12g of fat, and a total of 171 calories. A mixture of onion, mayonnaise, parsley, and a handful of other ingredients are all it takes to make this recipe so flavorful. 64 people were glad they tried this recipe. From preparation to the plate, this recipe takes approximately approximately 45 minutes. It is brought to you by Foodista. ",
                                            "title": "Easy Onion Cheese Rounds",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 24.75,
                                            "servings": 8,
                                            "image": "https://spoonacular.com/recipeImages/642041-556x370.jpg"
                                        },
                                        {
                                            "description": "The recipe Black Bean and Peppers Taco Filling is ready in roughly 45 minutes and is definitely an excellent gluten free and vegan option for lovers of Mexican food. For 52 cents per serving, this recipe covers 11% of your daily requirements of vitamins and minerals. This recipe makes 8 servings with 117 calories, 5g of protein, and 3g of fat each. This recipe is liked by 10 foodies and cooks. Head to the store and pick up chili powder, paprika, canned tomatoes, and a few other things to make it today.",
                                            "title": "Black Bean and Peppers Taco Filling",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 54.61,
                                            "servings": 8,
                                            "image": "https://spoonacular.com/recipeImages/635058-556x370.jpg"
                                        },
                                        {
                                            "description": "If you have around around 45 minutes to spend in the kitchen, Roasted Endive Salad With Prosciutto, Figs and Pistachios might be a spectacular gluten free, dairy free, paleolithic, and primal recipe to try. One serving contains 494 calories, 13g of protein, and 24g of fat. This recipe serves 4 and costs $3.64 per serving. If you have endive, figs, pistachio nuts, and a few other ingredients on hand, you can make it. 6 people were impressed by this recipe. It is brought to you by Foodista. It works well as a main course.",
                                            "title": "Roasted Endive Salad With Prosciutto, Figs and Pistachios",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 363.51,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/658579-556x370.jpg"
                                        },
                                        {
                                            "description": "Pecan Pumpkin Pie Dessert Pizza with Maple Whipped Cream might be just the Mediterranean recipe you are searching for. For $1.41 per serving, you get a dessert that serves 10. One serving contains 394 calories, 6g of protein, and 29g of fat. Thanksgiving will be even more special with this recipe. 25 people have tried and liked this recipe. From preparation to the plate, this recipe takes around 45 minutes. A mixture of brown sugar, pumpkin pie filling/mix, pecans, and a handful of other ingredients are all it takes to make this recipe so delicious.",
                                            "title": "Pecan Pumpkin Pie Dessert Pizza with Maple Whipped Cream",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 140.59,
                                            "servings": 10,
                                            "image": "https://spoonacular.com/recipeImages/655525-556x370.jpg"
                                        },
                                        {
                                            "description": "The recipe A Classic Caesar Salad could satisfy your American craving in roughly 45 minutes. One serving contains 1699 calories, 40g of protein, and 126g of fat. For $6.15 per serving, you get a main course that serves 1. 7 people have made this recipe and would make it again. Head to the store and pick up thickly crusty bread, tabasco sauce, romaine lettuce, and a few other things to make it today.",
                                            "title": "A Classic Caesar Salad",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 612.16,
                                            "servings": 1,
                                            "image": "https://spoonacular.com/recipeImages/631890-556x370.jpg"
                                        },
                                        {
                                            "description": "You can never have too many soup recipes, so give Shrimp and Lemongrass Soup a try. This recipe serves 4 and costs $1.68 per serving. One serving contains 123 calories, 9g of protein, and 3g of fat. If you have daikon, bean sprouts, mint, and a few other ingredients on hand, you can make it. It is a good option if you're following a gluten free, dairy free, whole 30, and pescatarian diet. It is brought to you by Foodista. It is perfect for Autumn. This recipe is liked by 13 foodies and cooks. From preparation to the plate, this recipe takes around around 45 minutes. Taking all factors into account, this recipe earns a spoonacular score of 75%, which is solid.",
                                            "title": "Shrimp and Lemongrass Soup",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 168.22,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/659934-556x370.jpg"
                                        },
                                        {
                                            "description": "Four-Berry Blast Fruit Smoothie might be just the morn meal you are searching for. This gluten free and vegetarian recipe serves 4 and costs $1.24 per serving. One serving contains 264 calories, 11g of protein, and 11g of fat. Only a few people made this recipe, and 5 would say it hit the spot. From preparation to the plate, this recipe takes approximately 10 minutes. Head to the store and pick up milk, raspberries, lemonade concentrate, and a few other things to make it today.",
                                            "title": "Four-Berry Blast Fruit Smoothie",
                                            "vegetarian": True,
                                            "time": 10,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 123.98,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/643241-556x370.jpg"
                                        },
                                        {
                                            "description": "You can never have too many main course recipes, so give Grilled Fish With Sun Dried Tomato Relish a try. One serving contains 703 calories, 42g of protein, and 25g of fat. This gluten free, dairy free, fodmap friendly, and pescatarian recipe serves 2 and costs $7.34 per serving. 16 people have tried and liked this recipe. It can be enjoyed any time, but it is especially good for The Fourth Of July. If you have pepper, extra virgin olive oil, salt, and a few other ingredients on hand, you can make it.",
                                            "title": "Grilled Fish With Sun Dried Tomato Relish",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 889.37,
                                            "servings": 2,
                                            "image": "https://spoonacular.com/recipeImages/645714-556x370.jpg"
                                        },
                                        {
                                            "description": "Need a gluten free and primal main course? Pesto Chicken Zoodles could be an amazing recipe to try. For $2.5 per serving, this recipe covers 26% of your daily requirements of vitamins and minerals. One serving contains 524 calories, 35g of protein, and 41g of fat. From preparation to the plate, this recipe takes roughly 45 minutes. 22 people have made this recipe and would make it again. Head to the store and pick up cajun seasoning, chicken breasts seasoned, olive oil, and a few other things to make it today.",
                                            "title": "Pesto Chicken Zoodles",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 274.6,
                                            "servings": 3,
                                            "image": "https://spoonacular.com/recipeImages/780001-556x370.jpg"
                                        },
                                        {
                                            "description": "Crispy Tiger Prawns With Honey and Garlic Sauce could be just the gluten free, dairy free, and pescatarian recipe you've been looking for. One serving contains 159 calories, 6g of protein, and 8g of fat. This recipe serves 3. For $1.16 per serving, this recipe covers 5% of your daily requirements of vitamins and minerals. From preparation to the plate, this recipe takes approximately approximately 45 minutes. 7 people have made this recipe and would make it again. A mixture of shao hsing wine, honey, egg yolk, and a handful of other ingredients are all it takes to make this recipe so flavorful. It is brought to you by Foodista.",
                                            "title": "Crispy Tiger Prawns With Honey and Garlic Sauce",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 116.12,
                                            "servings": 3,
                                            "image": "https://spoonacular.com/recipeImages/640844-556x370.jpg"
                                        },
                                        {
                                            "description": "The recipe Chicken En Papillote With Basil and Cherry Tomatoes can be made in around around 45 minutes. One portion of this dish contains roughly 25g of protein, 31g of fat, and a total of 434 calories. For $2.62 per serving, this recipe covers 18% of your daily requirements of vitamins and minerals. This recipe serves 1. 26 people found this recipe to be yummy and satisfying. Head to the store and pick up garnish: basil chiffonade, to 5 cherry tomatoes, olive oil, and a few other things to make it today. It is brought to you by Foodista. It is a good option if you're following a gluten free, dairy free, paleolithic, and primal diet.",
                                            "title": "Chicken En Papillote With Basil and Cherry Tomatoes",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 262.25,
                                            "servings": 1,
                                            "image": "https://spoonacular.com/recipeImages/638071-556x370.jpg"
                                        },
                                        {
                                            "description": "Buttermilk Onion Rings is a hor d'oeuvre that serves 3. One portion of this dish contains roughly 19g of protein, 327g of fat, and a total of 3262 calories. For $2.25 per serving, this recipe covers 29% of your daily requirements of vitamins and minerals. If you have vegetable oil, salt, baking powder, and a few other ingredients on hand, you can make it. 18 people have made this recipe and would make it again. It is brought to you by Foodista. From preparation to the plate, this recipe takes around around 45 minutes.",
                                            "title": "Buttermilk Onion Rings",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 224.72,
                                            "servings": 3,
                                            "image": "https://spoonacular.com/recipeImages/636558-556x370.jpg"
                                        },
                                        {
                                            "description": "If you want to add more gluten free and dairy free recipes to your recipe box, Ham with Orange Rosemary Marmalade Glaze might be a recipe you should try. One serving contains 3119 calories, 246g of protein, and 191g of fat. For $4.9 per serving, this recipe covers 58% of your daily requirements of vitamins and minerals. This recipe serves 4. This recipe from Foodista requires ham, orange marmalade, ginger, and brown sugar. 61 person were impressed by this recipe.",
                                            "title": "Ham with Orange Rosemary Marmalade Glaze",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 489.7,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/646217-556x370.jpg"
                                        },
                                        {
                                            "description": "Easy Asian Sweet Chili Chicken Meatballs might be just the main course you are searching for. Watching your figure? This dairy free recipe has 270 calories, 18g of protein, and 8g of fat per serving. For $1.52 per serving, this recipe covers 16% of your daily requirements of vitamins and minerals. From preparation to the plate, this recipe takes roughly 45 minutes. This recipe is typical of American cuisine. 12 people have made this recipe and would make it again. It will be a hit at your The Super Bowl event. Head to the store and pick up pepper flakes, rice wine vinegar, cornstarch, and a few other things to make it today. ",
                                            "title": "Easy Asian Sweet Chili Chicken Meatballs",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 137.32,
                                            "servings": 6,
                                            "image": "https://spoonacular.com/recipeImages/803061-556x370.jpg"
                                        },
                                        {
                                            "description": "One serving contains 169 calories, 0g of protein, and 5g of fat. For 77 cents per serving, this recipe covers 2% of your daily requirements of vitamins and minerals. This recipe is liked by 101 foodies and cooks. Head to the store and pick up basil leaves, strawberries, honey, and a few other things to make it today.",
                                            "title": "Strawberry Basil Sorbet (no Ice Cream Maker Necessary!)",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 76.94,
                                            "servings": 1,
                                            "image": "https://spoonacular.com/recipeImages/716424-556x370.jpg"
                                        },
                                        {
                                            "description": "Moroccan chickpean and lentil stew is a dairy free, lacto ovo vegetarian, and vegan main course. One portion of this dish contains around 20g of protein, 7g of fat, and a total of 467 calories. This recipe serves 3. For $1.34 per serving, this recipe covers 30% of your daily requirements of vitamins and minerals. 11 person found this recipe to be tasty and satisfying. It will be a hit at your Autumn event. This recipe from Foodista requires lemon juice, ground turmeric, carrots, and ground cumin.",
                                            "title": "Moroccan chickpea and lentil stew",
                                            "vegetarian": True,
                                            "time": 30,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 126.12,
                                            "servings": 3,
                                            "image": "https://spoonacular.com/recipeImages/652417-556x370.jpg"
                                        },
                                        {
                                            "description": "If you have about approximately 45 minutes to spend in the kitchen, Rustic Brie Toasts with Wild Mushroom, Cranberry and Shallot might be an excellent lacto ovo vegetarian recipe to try. This recipe serves 10 and costs 66 cents per serving. One serving contains 162 calories, 8g of protein, and 9g of fat. This recipe from Foodista requires wedge of beautiful brie cheese, rustic baguette, olive oil, and salt and pepper.",
                                            "title": "Rustic Brie Toasts with Wild Mushroom, Cranberry and Shallot",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 66.25,
                                            "servings": 10,
                                            "image": "https://spoonacular.com/recipeImages/658914-556x370.jpg"
                                        },
                                        {
                                            "description": "Apple & Cream Cheese Braid might be just the main course you are searching for. One serving contains 5803 calories, 122g of protein, and 244g of fat. This recipe serves 1 and costs $10.37 per serving. 7 people were impressed by this recipe. Head to the store and pick up butter, milk, butter, and a few other things to make it today.",
                                            "title": "Apple & Cream Cheese Braid",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 1036.55,
                                            "servings": 1,
                                            "image": "https://spoonacular.com/recipeImages/632452-556x370.jpg"
                                        },
                                        {
                                            "description": "Need a lacto ovo vegetarian hor d'oeuvre? Gluten Free Onion Rings could be an amazing recipe to try. This recipe serves 4. One serving contains 361 calories, 8g of protein, and 19g of fat. For 83 cents per serving, this recipe covers 8% of your daily requirements of vitamins and minerals. 38 people found this recipe to be yummy and satisfying. It is brought to you by Foodista. If you have egg, all purpose flour, salt, and a few other ingredients on hand, you can make it.",
                                            "title": "Gluten Free Onion Rings",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 83.07,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/644846-556x370.jpg"
                                        },
                                        {
                                            "description": "Roasted Cranberries, Ricotta & Honey Crostini might be just the hor d'oeuvre you are searching for. One serving contains 334 calories, 3g of protein, and 1g of fat. For 84 cents per serving, this recipe covers 6% of your daily requirements of vitamins and minerals. It can be enjoyed any time, but it is especially good for Christmas. This recipe is typical of Mediterranean cuisine. 548 people have made this recipe and would make it again. If you have roasted cranberry sauce, roasted cranberry sauce, honey, and a few other ingredients on hand, you can make it.",
                                            "title": "Roasted Cranberries, Ricotta & Honey Crostini",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 84.04,
                                            "servings": 1,
                                            "image": "https://spoonacular.com/recipeImages/716412-556x370.jpg"
                                        },
                                        {
                                            "description": "You can never have too many main course recipes, so give Easy Chicken, Kielbasan and Shrimp Paellan a try. This gluten free, dairy free, and fodmap friendly recipe serves 8 and costs $2.38 per serving. One serving contains 408 calories, 34g of protein, and 10g of fat. This recipe is typical of European cuisine. If you have picante sauce, chicken breast strips, ground turmeric, and a few other ingredients on hand, you can make it. 19 people have tried and liked this recipe. ",
                                            "title": "Easy Chicken, Kielbasa and Shrimp Paella",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 238.13,
                                            "servings": 8,
                                            "image": "https://spoonacular.com/recipeImages/641911-556x370.jpg"
                                        },
                                        {
                                            "description": "Coconut Macaroons With Chocolate Drizzle could be just the lacto ovo vegetarian recipe you've been looking for. This recipe serves 24. For 27 cents per serving, this recipe covers 3% of your daily requirements of vitamins and minerals. One portion of this dish contains roughly 2g of protein, 7g of fat, and a total of 156 calories. 10 people were impressed by this recipe. This recipe from Foodista requires condensed milk, coconut, salt, and vanillan extract. From preparation to the plate, this recipe takes roughly roughly 45 minutes.",
                                            "title": "Coconut Macaroons With Chocolate Drizzle",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 27.23,
                                            "servings": 24,
                                            "image": "https://spoonacular.com/recipeImages/639779-556x370.jpg"
                                        },
                                        {
                                            "description": "If you have roughly about 45 minutes to spend in the kitchen, Beans Hawaiian might be an amazing gluten free and dairy free recipe to try. This recipe serves 8 and costs $1.61 per serving. One portion of this dish contains about 29g of protein, 10g of fat, and a total of 442 calories. This recipe from Foodista requires navy beans, brown sugar, bacon, and ham steak. Not a lot of people made this recipe, and 6 would say it hit the spot.",
                                            "title": "Beans Hawaiian",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 161.29,
                                            "servings": 8,
                                            "image": "https://spoonacular.com/recipeImages/634545-556x370.jpg"
                                        },
                                        {
                                            "description": "Easy Baked Pork Chop is a gluten free, dairy free, and fodmap friendly main course. For $3.19 per serving, this recipe covers 31% of your daily requirements of vitamins and minerals. One serving contains 519 calories, 59g of protein, and 28g of fat. 404 people were impressed by this recipe. A mixture of soy sauce, worcestershire sauce, vegetable oil, and a handful of other ingredients are all it takes to make this recipe so flavorful.",
                                            "title": "Easy Baked Pork Chop",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 318.81,
                                            "servings": 3,
                                            "image": "https://spoonacular.com/recipeImages/715481-556x370.jpg"
                                        },
                                        {
                                            "description": "Lemon Coconut Granola might be just the morn meal you are searching for. Watching your figure? This gluten free, dairy free, and vegetarian recipe has 263 calories, 6g of protein, and 16g of fat per serving. For 56 cents per serving, this recipe covers 9% of your daily requirements of vitamins and minerals. 32 people have made this recipe and would make it again. If you have rolled oats, honey, currants, and a few other ingredients on hand, you can make it.",
                                            "title": "Lemon Coconut Granola",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 56.12,
                                            "servings": 15,
                                            "image": "https://spoonacular.com/recipeImages/649567-556x370.jpg"
                                        },
                                        {
                                            "description": "Roasted Cabbage Wedge Salad with Yogurt Gorgonzola Dressing might be just the main course you are searching for. One serving contains 187 calories, 12g of protein, and 11g of fat. This gluten free recipe serves 4 and costs $1.3 per serving. Several people made this recipe, and 550 would say it hit the spot. If you have bacon, scallions, gorgonzola, and a few other ingredients on hand, you can make it.",
                                            "title": "Roasted Cabbage Wedge Salad with Yogurt Gorgonzola Dressing",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 129.8,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/716430-556x370.jpg"
                                        },
                                        {
                                            "description": "Easy Baked Parmesan Chicken takes about about 45 minutes from beginning to end. This recipe makes 4 servings with 598 calories, 67g of protein, and 18g of fat each. For $3.51 per serving, this recipe covers 38% of your daily requirements of vitamins and minerals. It is brought to you by Foodista. 92 people were impressed by this recipe. If you have chicken breast halves, egg, parmesan cheese, and a few other ingredients on hand, you can make it.",
                                            "title": "Easy Baked Parmesan Chicken",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 351.25,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/641836-556x370.jpg"
                                        },
                                        {
                                            "description": "The recipe Healthy Vegan Red Velvet Brownies could satisfy your American craving in roughly 45 minutes. Watching your figure? This gluten free and vegan recipe has 182 calories, 5g of protein, and 5g of fat per serving. For 42 cents per serving, this recipe covers 8% of your daily requirements of vitamins and minerals. A couple people made this recipe, and 91 would say it hit the spot. It is perfect for valentin day. A mixture of cocoa powder, apple sauce, brown sugar, and a handful of other ingredients are all it takes to make this recipe so delicious.",
                                            "title": "Healthy Vegan Red Velvet Brownies",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 41.99,
                                            "servings": 8,
                                            "image": "https://spoonacular.com/recipeImages/646524-556x370.jpg"
                                        },
                                        {
                                            "description": "Need a gluten free, dairy free, lacto ovo vegetarian, and fodmap friendly dessert? Guf\" Danish Ice Cream Topping could be an excellent recipe to try. For 40 cents per serving, this recipe covers 2% of your daily requirements of vitamins and minerals. This recipe serves 4. One portion of this dish contains about 2g of protein, 0g of fat, and a total of 71 calories. 39 people were impressed by this recipe. It will be a hit at your Summer event. From preparation to the plate, this recipe takes around around 45 minutes. This recipe from Foodista requires , strawberries, sugar, and lemon juice.",
                                            "title": "Guf\" Danish Ice Cream Topping",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 39.5,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/631781-556x370.jpg"
                                        },
                                        {
                                            "description": "Banana Foster Bread Pudding requires roughly roughly 45 minutes from start to finish. This recipe serves 8 and costs $1.75 per serving. Watching your figure? This lacto ovo vegetarian recipe has 1040 calories, 12g of protein, and 45g of fat per serving. A couple people made this recipe, and 27 would say it hit the spot. This recipe from Foodista requires bananas, bananas, milk, and heavy cream. It works well as a dessert.",
                                            "title": "Banana Foster Bread Pudding",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 174.61,
                                            "servings": 8,
                                            "image": "https://spoonacular.com/recipeImages/634091-556x370.jpg"
                                        },
                                        {
                                            "description": "Need a gluten free and vegan main course? Easy Homemade Rice and Beans could be a great recipe to try. One serving contains 446 calories, 19g of protein, and 4g of fat. For $1.06 per serving, this recipe covers 26% of your daily requirements of vitamins and minerals. 471 person have made this recipe and would make it again. A mixture of olive oil, ground pepper, onion, and a handful of other ingredients are all it takes to make this recipe so yummy.",
                                            "title": "Easy Homemade Rice and Beans",
                                            "vegetarian": True,
                                            "time": 35,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 106.02,
                                            "servings": 2,
                                            "image": "https://spoonacular.com/recipeImages/716627-556x370.jpg"
                                        },
                                        {
                                            "description": "Valentine's Chicken Marsala might be a good recipe to expand your main course repertoire. This recipe serves 3 and costs $2.72 per serving. One serving contains 549 calories, 13g of protein, and 21g of fat. If you have mushrooms, olive oil, marsala wine, and a few other ingredients on hand, you can make it. 94 people were impressed by this recipe. It is brought to you by Foodista. From preparation to the plate, this recipe takes approximately approximately 45 minutes.",
                                            "title": "Valentine's Chicken Marsala",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 271.68,
                                            "servings": 3,
                                            "image": "https://spoonacular.com/recipeImages/664270-556x370.jpg"
                                        },
                                        {
                                            "description": "The recipe Popcorn Chicken is ready in about 45 minutes and is definitely a tremendous dairy free option for lovers of American food. This recipe serves 2 and costs $1.59 per serving. One serving contains 823 calories, 43g of protein, and 14g of fat. Plenty of people made this recipe, and 100 would say it hit the spot. It works well as a reasonably priced main course. If you have eggs, salt, chili powder, and a few other ingredients on hand, you can make it.",
                                            "title": "Popcorn Chicken",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 158.71,
                                            "servings": 2,
                                            "image": "https://spoonacular.com/recipeImages/716358-556x370.jpg"
                                        },
                                        {
                                            "description": "Need a gluten free and lacto ovo vegetarian side dish? Paneer Makhani could be an outstanding recipe to try. One serving contains 295 calories, 9g of protein, and 26g of fat. For $2.05 per serving, this recipe covers 4% of your daily requirements of vitamins and minerals. This recipe serves 4. This recipe from Foodista has 10 fans. Head to the store and pick up paneer, salt, cumin powder, and a few other things to make it today.",
                                            "title": "Paneer Makhani",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 205.38,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/654534-556x370.jpg"
                                        },
                                        {
                                            "description": "Forget going out to eat or ordering takeout every time you crave Mediterranean food. Try making Strawberry Cheesecake Chocolate Crepes at home. This recipe serves 4. One serving contains 638 calories, 16g of protein, and 38g of fat. For $1.69 per serving, this recipe covers 20% of your daily requirements of vitamins and minerals. This recipe from Pink When has 1928 fans. Several people really liked this breakfast. Mother's Day will be even more special with this recipe.",
                                            "title": "Strawberry Cheesecake Chocolate Crepes",
                                            "vegetarian": True,
                                            "time": 40,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 168.57,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/715569-556x370.jpg"
                                        },
                                        {
                                            "description": "If you have approximately 45 minutes to spend in the kitchen, Pierogi Casserole might be a tremendous lacto ovo vegetarian recipe to try. One portion of this dish contains around 31g of protein, 32g of fat, and a total of 814 calories. For $1.51 per serving, this recipe covers 29% of your daily requirements of vitamins and minerals. This recipe serves 4. It is brought to you by Pink When. Winter will be even more special with this recipe. This recipe is typical of Eastern European cuisine. This recipe is liked by 1545 foodies and cooks. Plenty of people really liked this main course. A mixture of butter, sharp cheddar cheese, potatoes, and a handful of other ingredients are all it takes to make this recipe so yummy.",
                                            "title": "Pierogi Casserole",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 155.09,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/715563-556x370.jpg"
                                        },
                                        {
                                            "description": "Pink Lemonade Crinkle Cookies might be just the dessert you are searching for. Watching your figure? This vegetarian recipe has 659 calories, 5g of protein, and 29g of fat per serving. For 54 cents per serving, this recipe covers 8% of your daily requirements of vitamins and minerals. Many people made this recipe, and 3229 would say it hit the spot.",
                                            "title": "Pink Lemonade Crinkle Cookies",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 53.93,
                                            "servings": 5,
                                            "image": "https://spoonacular.com/recipeImages/715541-556x370.jpg"
                                        },
                                        {
                                            "description": "The recipe How to Make Party Jollof Rice is ready in about 45 minutes and is definitely an amazing gluten free and vegan option for lovers of African food. For $1.35 per serving, this recipe covers 20% of your daily requirements of vitamins and minerals. This recipe makes 3 servings with 528 calories, 12g of protein, and 2g of fat each. Many people made this recipe, and 347 would say it hit the spot. If you have bay leaves, roma tomatoes, salt, and a few other ingredients on hand, you can make it.",
                                            "title": "How to Make Party Jollof Rice",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 122.98,
                                            "servings": 3,
                                            "image": "https://spoonacular.com/recipeImages/716298-556x370.jpg"
                                        },
                                        {
                                            "description": "Brownie Coffins takes roughly about 45 minutes from beginning to end. One portion of this dish contains about 5g of protein, 22g of fat, and a total of 358 calories. This recipe serves 5. For 56 cents per serving, this recipe covers 7% of your daily requirements of vitamins and minerals. A few people really liked this American dish. 15 people were glad they tried this recipe. It works well as a dessert.",
                                            "title": "Brownie Coffins",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 55.55,
                                            "servings": 5,
                                            "image": "https://spoonacular.com/recipeImages/636328-556x370.jpg"
                                        },
                                        {
                                            "description": "Cornmeal-Crusted Catfish with Cajun Seasoning and Spicy Tartar Sauce is a main course that serves 4. One portion of this dish contains roughly 27g of protein, 26g of fat, and a total of 420 calories. For $2.87 per serving, this recipe covers 26% of your daily requirements of vitamins and minerals. Not a lot of people made this recipe, and 8 would say it hit the spot. This recipe is typical of Cajun cuisine. From preparation to the plate, this recipe takes around around 45 minutes. If you have granulated garlic, dill pickle juice, scallion, and a few other ingredients on hand, you can make it. It is brought to you by Foodista. It is a good option if you're following a gluten free and pescatarian diet.",
                                            "title": "Cornmeal-Crusted Catfish with Cajun Seasoning and Spicy Tartar Sauce",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 287.28,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/640166-556x370.jpg"
                                        },
                                        {
                                            "description": "Bacon Wrapped Pork Tenderloin is a caveman, gluten free, dairy free, and primal main course. For $2.2 per serving, this recipe covers 30% of your daily requirements of vitamins and minerals. One serving contains 411 calories, 51g of protein, and 21g of fat. A couple people made this recipe, and 55 would say it hit the spot. If you have garlic powder, pepper, sage, and a few other ingredients on hand, you can make it.",
                                            "title": "Bacon Wrapped Pork Tenderloin",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 257.42,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/633344-556x370.jpg"
                                        },
                                        {
                                            "description": "Vegan Dirty Chai Pudding is a gluten free and dairy free recipe with 6 servings. One serving contains 325 calories, 5g of protein, and 22g of fat. For $1.93 per serving, this recipe covers 16% of your daily requirements of vitamins and minerals. It works well as a dessert. 6 people have made this recipe and would make it again. This recipe from Foodista requires pudding, cinnamon, vanilla, and cocoa powder.",
                                            "title": "Vegan Dirty Chai Pudding",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 193.28,
                                            "servings": 6,
                                            "image": "https://spoonacular.com/recipeImages/664429-556x370.jpg"
                                        },
                                        {
                                            "description": "You can never have too many Mediterranean recipes, so give Ratatouille With Brie a try. This main course has 490 calories, 14g of protein, and 45g of fat per serving. This gluten free, lacto ovo vegetarian, and primal recipe serves 4 and costs $1.97 per serving. If you have brie log such as alouette, plum tomatoes, zucchini, and a few other ingredients on hand, you can make it. This recipe from Foodista has 63 fans. From preparation to the plate, this recipe takes around around 45 minutes.",
                                            "title": "Ratatouille With Brie",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 196.79,
                                            "servings": 4,
                                            "image": "https://spoonacular.com/recipeImages/657939-556x370.jpg"
                                        },
                                        {
                                            "description": "Need a gluten free, dairy free, and whole 30 main course? Peri Peri Chicken and Savoury Rice could be an amazing recipe to try. This recipe makes 6 servings with 643 calories, 40g of protein, and 50g of fat each. For $1.64 per serving, this recipe covers 24% of your daily requirements of vitamins and minerals. 336 people have made this recipe and would make it again. If you have sized lemon, chicken pieces, oregano, and a few other ingredients on hand, you can make it.",
                                            "title": "Peri Peri Chicken and Savoury Rice",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 143.05,
                                            "servings": 6,
                                            "image": "https://spoonacular.com/recipeImages/716296-556x370.jpg"
                                        },
                                        {
                                            "description": "The recipe Savory Cheese Dill Scones could satisfy your Scottish craving in roughly 45 minutes. One serving contains 215 calories, 6g of protein, and 11g of fat. This recipe serves 12 and costs 30 cents per serving. It works well as an inexpensive morn meal. 40 people have tried and liked this recipe. A mixture of cottage cheese, a pinch of baking soda, pepper, and a handful of other ingredients are all it takes to make this recipe so tasty. It is a good option if you're following a vegetarian diet.",
                                            "title": "Savory Cheese Dill Scones",
                                            "vegetarian": True,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 29.57,
                                            "servings": 12,
                                            "image": "https://spoonacular.com/recipeImages/659463-556x370.jpg"
                                        },
                                        {
                                            "description": "Steak with lemon and capers might be just the main course you are searching for. One serving contains 951 calories, 47g of protein, and 54g of fat. For $6.49 per serving, this recipe covers 32% of your daily requirements of vitamins and minerals. From preparation to the plate, this recipe takes roughly 45 minutes. 9 people were impressed by this recipe. It can be enjoyed any time, but it is especially good for valentin day. A mixture of flour, garlic, lemon wedges, and a handful of other ingredients are all it takes to make this recipe so flavorful.",
                                            "title": "Steak with lemon and capers",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": False,
                                            "pricePerServing": 646.43,
                                            "servings": 2,
                                            "image": "https://spoonacular.com/recipeImages/661531-556x370.jpg"
                                        },
                                        {
                                            "description": "Chicken Suya might be just the main course you are searching for. This recipe serves 1 and costs $3.22 per serving. Watching your figure? This gluten free, dairy free, and whole 30 recipe has 1070 calories, 87g of protein, and 71g of fat per serving. If you have chicken, salt, cooking spoon groundnut oil, and a few other ingredients on hand, you can make it.",
                                            "title": "Chicken Suya",
                                            "vegetarian": False,
                                            "time": 45,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 186.02,
                                            "servings": 1,
                                            "image": "https://spoonacular.com/recipeImages/716342-556x370.jpg"
                                        },
                                        {
                                            "description": "The recipe Chicken and Sausage Jambalayan is ready in approximately 1 hour and 15 minutes and is definitely an amazing gluten free and dairy free option for lovers of Creole food. One serving contains 636 calories, 27g of protein, and 31g of fat. For $1.86 per serving, you get a main course that serves 8. 2169 people have made this recipe and would make it again. Head to the store and pick up pepper, sausage, water, and a few other things to make it today. ",
                                            "title": "Chicken and Sausage Jambalaya",
                                            "vegetarian": False,
                                            "time": 75,
                                            "cheap": False,
                                            "glutenfree": True,
                                            "pricePerServing": 188.06,
                                            "servings": 8,
                                            "image": "https://spoonacular.com/recipeImages/715545-556x370.jpg"
                                        }
                                    ]
                        )
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the locations table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_recipes():
    db.session.execute('TRUNCATE recipes;')
    db.session.commit()
