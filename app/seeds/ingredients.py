from app.models import db, Ingredient


# Adds a demo location, you can add other locations here if you want

def seed_ingredients():

    db.session.bulk_insert_mappings(Ingredient,
                                    [
                                        {
                                            "recipeId": 1,
                                            "ingredientName": "Bacon cut in strips",
                                            "amount": 1.0,
                                            "unit": "oz."
                                        },
                                        {
                                            "recipeId": 1,
                                            "ingredientName": "All Natural Tomato soup",
                                            "amount": 1.0,
                                            "unit": "can"
                                        },
                                        {
                                            "recipeId": 1,
                                            "ingredientName": "Vegetable Stock",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 1,
                                            "ingredientName": "Alouette All Natural Sundried Tomato and Basil soft spreadable cheese",
                                            "amount": 6.5,
                                            "unit": "oz"
                                        },
                                        {
                                            "recipeId": 2,
                                            "ingredientName": "Pre-made fresh agnolotti/ravioli",
                                            "amount": 13.0,
                                            "unit": "oz"
                                        },
                                        {
                                            "recipeId": 2,
                                            "ingredientName": "egg",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 2,
                                            "ingredientName": "breadcrumbs",
                                            "amount": 1.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 3,
                                            "ingredientName": "Sweet yellow onion, finely chopped",
                                            "amount": 0.5,
                                            "unit": "small"
                                        },
                                        {
                                            "recipeId": 3,
                                            "ingredientName": "Mayonnaise",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 3,
                                            "ingredientName": "Parmesan cheese, freshly grated",
                                            "amount": 3.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 3,
                                            "ingredientName": "Fresh parsley, finely chopped",
                                            "amount": 2.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 3,
                                            "ingredientName": "Sea salt and freshly ground pepper",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 3,
                                            "ingredientName": "White bread",
                                            "amount": 8.0,
                                            "unit": "slices"
                                        },
                                        {
                                            "recipeId": 4,
                                            "ingredientName": "Bell pepper, diced",
                                            "amount": 1.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 4,
                                            "ingredientName": "Black beans, rinsed and drained",
                                            "amount": 14.0,
                                            "unit": "ounce"
                                        },
                                        {
                                            "recipeId": 4,
                                            "ingredientName": "Crushed tomatoes",
                                            "amount": 28.0,
                                            "unit": "ounce"
                                        },
                                        {
                                            "recipeId": 4,
                                            "ingredientName": "Chili powder",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 4,
                                            "ingredientName": "Garlic powder",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 4,
                                            "ingredientName": "Ground cumin",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 4,
                                            "ingredientName": "Light or extra-virgin olive oil",
                                            "amount": 1.5,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 4,
                                            "ingredientName": "Chopped onion",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 4,
                                            "ingredientName": "Dried oregano",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 4,
                                            "ingredientName": "Paprika",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 5,
                                            "ingredientName": "endive (green, red or both)",
                                            "amount": 6.0,
                                            "unit": "heads"
                                        },
                                        {
                                            "recipeId": 5,
                                            "ingredientName": "olive oil (an infused oil, such as roasted garlic olive",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 5,
                                            "ingredientName": "prosciutto",
                                            "amount": 2.0,
                                            "unit": "slices"
                                        },
                                        {
                                            "recipeId": 5,
                                            "ingredientName": "dried figs, sliced as thinly as possible",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 5,
                                            "ingredientName": "pistachio nuts, shells removed",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 5,
                                            "ingredientName": "organic honey",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 6,
                                            "ingredientName": "brown sugar",
                                            "amount": 2.0,
                                            "unit": "Tbs"
                                        },
                                        {
                                            "recipeId": 6,
                                            "ingredientName": "butter",
                                            "amount": 2.0,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 6,
                                            "ingredientName": "heavy cream",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 6,
                                            "ingredientName": "maple syrup",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 6,
                                            "ingredientName": "shelled pecans",
                                            "amount": 8.0,
                                            "unit": "ounces"
                                        },
                                        {
                                            "recipeId": 6,
                                            "ingredientName": "Mama Mary's Mini Original Pizza Crust",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 6,
                                            "ingredientName": "canned Pumpkin pie filling/mix",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 6,
                                            "ingredientName": "pumpkin pie spice",
                                            "amount": 0.25,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 7,
                                            "ingredientName": "thickly sliced crusty bread",
                                            "amount": 150.0,
                                            "unit": "g"
                                        },
                                        {
                                            "recipeId": 7,
                                            "ingredientName": "egg yolk",
                                            "amount": 2.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 7,
                                            "ingredientName": "extra virgin olive oil",
                                            "amount": 60.0,
                                            "unit": "ml"
                                        },
                                        {
                                            "recipeId": 7,
                                            "ingredientName": "lemon juice",
                                            "amount": 30.0,
                                            "unit": "ml"
                                        },
                                        {
                                            "recipeId": 7,
                                            "ingredientName": "English mustard powder",
                                            "amount": 5.0,
                                            "unit": "ml"
                                        },
                                        {
                                            "recipeId": 7,
                                            "ingredientName": "Freshly grated Parmesan cheese",
                                            "amount": 25.0,
                                            "unit": "g"
                                        },
                                        {
                                            "recipeId": 7,
                                            "ingredientName": "Romaine lettuce, trimmed and washed",
                                            "amount": 1.0,
                                            "unit": "head"
                                        },
                                        {
                                            "recipeId": 7,
                                            "ingredientName": "sunflower oil",
                                            "amount": 45.0,
                                            "unit": "ml"
                                        },
                                        {
                                            "recipeId": 7,
                                            "ingredientName": "Tabasco sauce",
                                            "amount": 5.0,
                                            "unit": "ml"
                                        },
                                        {
                                            "recipeId": 7,
                                            "ingredientName": "Worcestershire sauce",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 8,
                                            "ingredientName": "raw jumbo shrimp, peeled and deviened, peels reserved",
                                            "amount": 6.0,
                                            "unit": "jumbo"
                                        },
                                        {
                                            "recipeId": 8,
                                            "ingredientName": "lemongrass stems",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 8,
                                            "ingredientName": "scallion, thinly sliced",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 8,
                                            "ingredientName": "bean sprouts",
                                            "amount": 1.0,
                                            "unit": "c"
                                        },
                                        {
                                            "recipeId": 8,
                                            "ingredientName": "lime, juiced",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 8,
                                            "ingredientName": "carrot, peeled and julienned",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 8,
                                            "ingredientName": "daikon, peeled and julienned",
                                            "amount": 0.5,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 8,
                                            "ingredientName": "chicken stock",
                                            "amount": 4.0,
                                            "unit": "c"
                                        },
                                        {
                                            "recipeId": 8,
                                            "ingredientName": "Mint, for garnish",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 9,
                                            "ingredientName": "frozen blackberries",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 9,
                                            "ingredientName": "frozen blueberries",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 9,
                                            "ingredientName": "lemonade concentrate",
                                            "amount": 2.0,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 9,
                                            "ingredientName": "frozen unsweetened raspberries",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 9,
                                            "ingredientName": "frozen unsweetened strawberries",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 9,
                                            "ingredientName": "sugar",
                                            "amount": 1.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 9,
                                            "ingredientName": "vanilla extract",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 9,
                                            "ingredientName": "whole milk (do not use skim)",
                                            "amount": 5.5,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "balsamic vinegar",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "cucumber",
                                            "amount": 150.0,
                                            "unit": "g"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "extra virgin olive oil",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "mint or basil",
                                            "amount": 5.0,
                                            "unit": "leaves"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "olive oil",
                                            "amount": 2.0,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "pepper",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "salt",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "sesame seeds",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "Sugar",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "sun-dried tomatoes in oil (oil drained)",
                                            "amount": 120.0,
                                            "unit": "g"
                                        },
                                        {
                                            "recipeId": 10,
                                            "ingredientName": "firm white fish fillet (I used kingklip)",
                                            "amount": 400.0,
                                            "unit": "g"
                                        },
                                        {
                                            "recipeId": 11,
                                            "ingredientName": "Cajun seasoning",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 11,
                                            "ingredientName": "chicken breasts",
                                            "amount": 16.0,
                                            "unit": "oz"
                                        },
                                        {
                                            "recipeId": 11,
                                            "ingredientName": "fresh basil leaves",
                                            "amount": 0.75,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 11,
                                            "ingredientName": "garlic, peeled",
                                            "amount": 1.0,
                                            "unit": "clove"
                                        },
                                        {
                                            "recipeId": 11,
                                            "ingredientName": "garlic salt",
                                            "amount": 1.0,
                                            "unit": "Tbsp"
                                        },
                                        {
                                            "recipeId": 11,
                                            "ingredientName": "olive oil",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 11,
                                            "ingredientName": "grated parmesan cheese",
                                            "amount": 1.0,
                                            "unit": "Tbsp"
                                        },
                                        {
                                            "recipeId": 11,
                                            "ingredientName": "salt and pepper to taste",
                                            "amount": 3.0,
                                            "unit": "servings"
                                        },
                                        {
                                            "recipeId": 11,
                                            "ingredientName": "zucchini, spiraled",
                                            "amount": 2.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "tiger prawns, peeled and de-veined (leave tails intact)",
                                            "amount": 10.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "cornflour",
                                            "amount": 3.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "water",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "light soy sauce",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "egg yolk, lightly beaten",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "sesame oil",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "Vegetable oil for deep-frying",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "Spring onion (green onion), sliced on the diagonal (for garnish)",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "honey",
                                            "amount": 2.0,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "shao hsing wine or dry sherry",
                                            "amount": 2.0,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "garlic cloves, finely diced",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 12,
                                            "ingredientName": "light soy sauce",
                                            "amount": 5.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 13,
                                            "ingredientName": "boneless chicken breast (with or skinless)",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 13,
                                            "ingredientName": "salt and pepper, to taste",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 13,
                                            "ingredientName": "olive oil",
                                            "amount": 2.0,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 13,
                                            "ingredientName": "onion, sliced",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 13,
                                            "ingredientName": "garlic clove, sliced",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 13,
                                            "ingredientName": "white wine",
                                            "amount": 2.0,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 13,
                                            "ingredientName": "to 5 cherry tomatoes, halved",
                                            "amount": 4.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 13,
                                            "ingredientName": "basil, chiffonade",
                                            "amount": 2.0,
                                            "unit": "leaves"
                                        },
                                        {
                                            "recipeId": 13,
                                            "ingredientName": "Garnish: fresh basil chiffonade",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "sweet Vidalia onion, cut into slices",
                                            "amount": 1.0,
                                            "unit": "inch"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "all-purpose flour",
                                            "amount": 1.25,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "baking powder",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "salt",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "egg",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "buttermilk, or as needed",
                                            "amount": 1.5,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "dry unflavored bread crumbs",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "panko bread crumbs",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "Salt, to taste",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "vegetable oil (or as needed)",
                                            "amount": 1.0,
                                            "unit": "quart"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "Sriracha Hot Chili Sauce",
                                            "amount": 1.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 14,
                                            "ingredientName": "Crema Mexicana",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 15,
                                            "ingredientName": "smoked bone-in ham",
                                            "amount": 10.0,
                                            "unit": "pounds"
                                        },
                                        {
                                            "recipeId": 15,
                                            "ingredientName": "Zest of orange",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 15,
                                            "ingredientName": "apple cider",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 15,
                                            "ingredientName": "apple juice",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 15,
                                            "ingredientName": "orange juice",
                                            "amount": 2.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 15,
                                            "ingredientName": "orange marmalade",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 15,
                                            "ingredientName": "packed brown sugar",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 15,
                                            "ingredientName": "fresh rosemary, about 1 tablespoon",
                                            "amount": 1.0,
                                            "unit": "sprig"
                                        },
                                        {
                                            "recipeId": 15,
                                            "ingredientName": "fresh ginger, minced",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "bell pepper, diced",
                                            "amount": 1.0,
                                            "unit": "small"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "cabbage, diced",
                                            "amount": 0.33,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "carrot, grated",
                                            "amount": 1.0,
                                            "unit": "small"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "cornstarch",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "egg",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "fresh grated ginger (or powder)",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "garlic powder",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "green onion sprigs",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "ground chicken",
                                            "amount": 1.0,
                                            "unit": "lb"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "honey",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "low sodium soy sauce",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "onion powder",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "pineapple juice",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "red pepper flakes",
                                            "amount": 1.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "rice wine vinegar",
                                            "amount": 1.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "low sodium teriyaki sauce",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 16,
                                            "ingredientName": "low sodium, whole wheat bread crumbs",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 17,
                                            "ingredientName": "about finely chopped basil leaves",
                                            "amount": 0.25,
                                            "unit": "c"
                                        },
                                        {
                                            "recipeId": 17,
                                            "ingredientName": "basil oil (optional)",
                                            "amount": 1.0,
                                            "unit": "t"
                                        },
                                        {
                                            "recipeId": 17,
                                            "ingredientName": "honey or agave",
                                            "amount": 2.0,
                                            "unit": "T"
                                        },
                                        {
                                            "recipeId": 17,
                                            "ingredientName": "organic strawberries",
                                            "amount": 1.0,
                                            "unit": "bag"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "broccoli",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "chickpeas, rinsed and drained",
                                            "amount": 1.0,
                                            "unit": "can"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "carrots, chopped",
                                            "amount": 2.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "celery stalks",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "cooked lentils",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "couscous",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "Fresh cilantro, optional",
                                            "amount": 3.0,
                                            "unit": "servings"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "ground cinnamon",
                                            "amount": 0.125,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "ground cumin",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "ground turmeric",
                                            "amount": 0.5,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "lemon juice",
                                            "amount": 1.0,
                                            "unit": "Tbs"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "olive oil",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "paprika",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "Salt and pepper",
                                            "amount": 3.0,
                                            "unit": "servings"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "tomato paste",
                                            "amount": 2.0,
                                            "unit": "Tbs"
                                        },
                                        {
                                            "recipeId": 18,
                                            "ingredientName": "water",
                                            "amount": 1.5,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 19,
                                            "ingredientName": "wild mushrooms",
                                            "amount": 2.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 19,
                                            "ingredientName": "shallot (finely diced)",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 19,
                                            "ingredientName": "dried cranberry (juice sweetened if possible)",
                                            "amount": 0.25,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 19,
                                            "ingredientName": "fresh thyme (finely minced)",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 19,
                                            "ingredientName": "rustic baguette",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 19,
                                            "ingredientName": "olive oil",
                                            "amount": 1.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 19,
                                            "ingredientName": "wedge of brie cheese",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 19,
                                            "ingredientName": "Pinch of salt and pepper",
                                            "amount": 1.0,
                                            "unit": "pinch"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "all purpose flour",
                                            "amount": 5.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "blanched sliced almonds",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "Sweet-Roll Dough",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "brown sugar",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "butter, softened",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "cinnamon",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "cream cheese",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "dry yeast",
                                            "amount": 2.0,
                                            "unit": "packages"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "egg, beaten with 1 water",
                                            "amount": 1.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "egg yolk",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "eggs",
                                            "amount": 3.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "Granny Smith Applies",
                                            "amount": 3.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "Grated lemon rind",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "milk, warmed",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "salt",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "sugar",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "sugar",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "unsalted butter",
                                            "amount": 2.0,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "Vanilla",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "warm water",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 20,
                                            "ingredientName": "Mix together until smooth",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 21,
                                            "ingredientName": "egg",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 21,
                                            "ingredientName": "vegetable oil",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 21,
                                            "ingredientName": "milk",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 21,
                                            "ingredientName": "gluten free pizza flour mix",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 21,
                                            "ingredientName": "salt",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 21,
                                            "ingredientName": "baking powder",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 21,
                                            "ingredientName": "yellow onions, sliced & separated into rings",
                                            "amount": 2.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 21,
                                            "ingredientName": "gluten free all purpose flour (for coating onions)",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 21,
                                            "ingredientName": "Oil for frying",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 22,
                                            "ingredientName": "peasant bread",
                                            "amount": 1.0,
                                            "unit": "slice"
                                        },
                                        {
                                            "recipeId": 22,
                                            "ingredientName": "fresh-ground pepper",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 22,
                                            "ingredientName": "honey",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 22,
                                            "ingredientName": "ricotta",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 22,
                                            "ingredientName": "ricotta",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 22,
                                            "ingredientName": "sea salt",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 22,
                                            "ingredientName": "roasted cranberry sauce",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 23,
                                            "ingredientName": "Fully-cooked chicken breast strips",
                                            "amount": 10.0,
                                            "unit": "ounces"
                                        },
                                        {
                                            "recipeId": 23,
                                            "ingredientName": "Swanson Chicken Broth or Swanson Chicken Stock, heated",
                                            "amount": 4.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 23,
                                            "ingredientName": "ground turmeric",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 23,
                                            "ingredientName": "Pace Picante Sauce",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 23,
                                            "ingredientName": "uncooked regular long-grain white rice",
                                            "amount": 2.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 23,
                                            "ingredientName": "frozen peeled, deveined, cooked shrimp, thawed",
                                            "amount": 0.75,
                                            "unit": "pound"
                                        },
                                        {
                                            "recipeId": 23,
                                            "ingredientName": "package turkey kielbasa, sliced",
                                            "amount": 16.0,
                                            "unit": "ounces"
                                        },
                                        {
                                            "recipeId": 23,
                                            "ingredientName": "vegetable oil",
                                            "amount": 1.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 24,
                                            "ingredientName": "all-purpose flour",
                                            "amount": 0.66,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 24,
                                            "ingredientName": "flaked coconut",
                                            "amount": 5.5,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 24,
                                            "ingredientName": "salt",
                                            "amount": 0.25,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 24,
                                            "ingredientName": "vanilla extract",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 24,
                                            "ingredientName": "can sweetened condensed milk",
                                            "amount": 14.0,
                                            "unit": "oz"
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "dried navy beans",
                                            "amount": 2.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "teriyaki sauce",
                                            "amount": 1.5,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "soy sauce",
                                            "amount": 1.0,
                                            "unit": "Tbsp"
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "pineapple juice",
                                            "amount": 0.66,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "brown sugar",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "fresly grated ginger",
                                            "amount": 1.0,
                                            "unit": "Tsp"
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "thick cut bacon",
                                            "amount": 6.0,
                                            "unit": "slices"
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "onion, finely diced",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "garlic clove, minced",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "fresh pineapple, roughly chopped",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 25,
                                            "ingredientName": "ham steak, cubed",
                                            "amount": 16.0,
                                            "unit": "oz"
                                        },
                                        {
                                            "recipeId": 26,
                                            "ingredientName": "ketchup",
                                            "amount": 2.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 26,
                                            "ingredientName": "lemon juice",
                                            "amount": 1.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 26,
                                            "ingredientName": "cut pork chops",
                                            "amount": 6.0,
                                            "unit": "medium"
                                        },
                                        {
                                            "recipeId": 26,
                                            "ingredientName": "soy sauce",
                                            "amount": 1.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 26,
                                            "ingredientName": "vegetable oil",
                                            "amount": 2.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 26,
                                            "ingredientName": "worcestershire sauce",
                                            "amount": 2.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 27,
                                            "ingredientName": "coconut oil",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 27,
                                            "ingredientName": "desiccated coconut",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 27,
                                            "ingredientName": "dried currants (or other dried fruit)",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 27,
                                            "ingredientName": "flax seeds",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 27,
                                            "ingredientName": "honey",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 27,
                                            "ingredientName": "Juice of lemons",
                                            "amount": 3.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 27,
                                            "ingredientName": "Peel of lemon",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 27,
                                            "ingredientName": "chopped nuts (almonds, hazelnuts, pistachios)",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 27,
                                            "ingredientName": "rolled oats",
                                            "amount": 3.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "bacon (optional)",
                                            "amount": 2.0,
                                            "unit": "strips"
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "garlic, minced",
                                            "amount": 1.0,
                                            "unit": "clove"
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "crumbled Gorgonzola* (or other blue cheese)",
                                            "amount": 0.66,
                                            "unit": "c"
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "chopped grape tomatoes",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "extra virgin olive oil or grapeseed oil",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "green cabbage, tough outer leaves removed",
                                            "amount": 0.5,
                                            "unit": "head"
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "juice lemon",
                                            "amount": 0.5,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "plain Greek yogurt",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "salt and freshly-ground pepper",
                                            "amount": 4.0,
                                            "unit": "servings"
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "chopped scallions",
                                            "amount": 1.0,
                                            "unit": "T"
                                        },
                                        {
                                            "recipeId": 28,
                                            "ingredientName": "chopped scallions",
                                            "amount": 2.0,
                                            "unit": "T"
                                        },
                                        {
                                            "recipeId": 29,
                                            "ingredientName": "boneless, skinless chicken breast halves",
                                            "amount": 8.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 29,
                                            "ingredientName": "egg, slightly beaten",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 29,
                                            "ingredientName": "Italian bread crumbs",
                                            "amount": 1.5,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 29,
                                            "ingredientName": "pasta sauce",
                                            "amount": 1.0,
                                            "unit": "jar"
                                        },
                                        {
                                            "recipeId": 29,
                                            "ingredientName": "mozzarella cheese, shredded",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 29,
                                            "ingredientName": "Parmesan cheese, grated",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "almond extract",
                                            "amount": 0.5,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "apple sauce",
                                            "amount": 4.0,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "baking powder",
                                            "amount": 0.75,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "baking soda",
                                            "amount": 0.125,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "cooked beets",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "brown sugar",
                                            "amount": 0.75,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "cocoa powder",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "ground flaxseed",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "red kidney beans",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "salt",
                                            "amount": 0.125,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 30,
                                            "ingredientName": "vanilla extract",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 31,
                                            "ingredientName": "frozen strawberries",
                                            "amount": 0.25,
                                            "unit": "lb"
                                        },
                                        {
                                            "recipeId": 31,
                                            "ingredientName": "sugar",
                                            "amount": 0.125,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 31,
                                            "ingredientName": "pasteurized egg whites",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 31,
                                            "ingredientName": "powdered sugar",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 31,
                                            "ingredientName": "lemon juice",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Butter (room temp)",
                                            "amount": 0.5,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Brown Sugar",
                                            "amount": 1.5,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Eggs",
                                            "amount": 3.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Bread (I used a brioche roll)",
                                            "amount": 1.0,
                                            "unit": "lb"
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Heavy Cream",
                                            "amount": 2.0,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Milk",
                                            "amount": 1.5,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Cream De Banana Liqueur",
                                            "amount": 1.0,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Ground Cinnamon",
                                            "amount": 2.0,
                                            "unit": "Tsp"
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Vanilla",
                                            "amount": 1.0,
                                            "unit": "Tsp"
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Bananas (sliced)",
                                            "amount": 6.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Bananas (sliced)",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Butter",
                                            "amount": 0.25,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 32,
                                            "ingredientName": "Brown Sugar",
                                            "amount": 1.0,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 33,
                                            "ingredientName": "black beans, not drained",
                                            "amount": 15.0,
                                            "unit": "ounce"
                                        },
                                        {
                                            "recipeId": 33,
                                            "ingredientName": "Tomatoes with diced green chilies, not drained",
                                            "amount": 10.0,
                                            "unit": "ounce"
                                        },
                                        {
                                            "recipeId": 33,
                                            "ingredientName": "chili powder",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 33,
                                            "ingredientName": "cumin",
                                            "amount": 0.5,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 33,
                                            "ingredientName": "ground black pepper",
                                            "amount": 0.25,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 33,
                                            "ingredientName": "optional: of hot sauce",
                                            "amount": 4.0,
                                            "unit": "dashes"
                                        },
                                        {
                                            "recipeId": 33,
                                            "ingredientName": "olive oil",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 33,
                                            "ingredientName": "onion, chopped",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 33,
                                            "ingredientName": "uncooked rice",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 33,
                                            "ingredientName": "water",
                                            "amount": 3.0,
                                            "unit": "Tbsp"
                                        },
                                        {
                                            "recipeId": 34,
                                            "ingredientName": "sliced, fresh mushrooms",
                                            "amount": 6.0,
                                            "unit": "oz"
                                        },
                                        {
                                            "recipeId": 34,
                                            "ingredientName": "boneless, skinless chicken breast",
                                            "amount": 1.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 34,
                                            "ingredientName": "garlic, minced",
                                            "amount": 2.0,
                                            "unit": "large cloves"
                                        },
                                        {
                                            "recipeId": 34,
                                            "ingredientName": "butter",
                                            "amount": 2.0,
                                            "unit": "Tbs"
                                        },
                                        {
                                            "recipeId": 34,
                                            "ingredientName": "olive oil",
                                            "amount": 1.0,
                                            "unit": "Tbs"
                                        },
                                        {
                                            "recipeId": 34,
                                            "ingredientName": "Seasoned Breadcrumbs/Coating Mix",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 34,
                                            "ingredientName": "Marsala wine",
                                            "amount": 2.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 34,
                                            "ingredientName": "heavy cream",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 34,
                                            "ingredientName": "Cooked pasta, if desired",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "all purpose flour",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "black pepper",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "breadcrumbs",
                                            "amount": 2.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "chopped chicken breast",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "chili powder",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "eggs",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "garlic clove",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "ginger powder",
                                            "amount": 0.25,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "seasoning cubes",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "Oil for deep frying",
                                            "amount": 2.0,
                                            "unit": "servings"
                                        },
                                        {
                                            "recipeId": 35,
                                            "ingredientName": "Pinch of Salt",
                                            "amount": 1.0,
                                            "unit": "pinch"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "cubed paneer (Indian Cottage cheese)",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "onion, skinless",
                                            "amount": 1.0,
                                            "unit": "medium"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "garlic",
                                            "amount": 1.0,
                                            "unit": "clove"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "grated ginger",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "turmeric powder",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "coriander powder",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "cumin powder",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "Tomato Paste, mixed thoroughly in a cup of water",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "kasuri methi (dried fenugreek leaves)",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "heavy whipping cream",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "salt to taste",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "sugar",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "canola oil",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 36,
                                            "ingredientName": "Kashmiri mirch ( Kashmiri Red Chilli Powder)",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "cream cheese",
                                            "amount": 8.0,
                                            "unit": "oz"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "diced strawberries",
                                            "amount": 1.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "vanilla extract",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "lemon juice",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "granulated sugar",
                                            "amount": 2.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "all-purpose flour",
                                            "amount": 1.5,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "cocoa powder unsweetened",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "kosher salt",
                                            "amount": 0.125,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "eggs",
                                            "amount": 3.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "milk",
                                            "amount": 1.25,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "water",
                                            "amount": 0.25,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "unsalted butter melted",
                                            "amount": 4.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 37,
                                            "ingredientName": "vanilla extract",
                                            "amount": 0.5,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 38,
                                            "ingredientName": "butter",
                                            "amount": 4.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 38,
                                            "ingredientName": "milk",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 38,
                                            "ingredientName": "onions, sliced",
                                            "amount": 2.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 38,
                                            "ingredientName": "salt and pepper to taste",
                                            "amount": 4.0,
                                            "unit": "servings"
                                        },
                                        {
                                            "recipeId": 38,
                                            "ingredientName": "sharp cheddar cheese, shredded",
                                            "amount": 1.5,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 38,
                                            "ingredientName": "white potatoes, peeled, cubed and then boiled until tender",
                                            "amount": 1.0,
                                            "unit": "lb"
                                        },
                                        {
                                            "recipeId": 38,
                                            "ingredientName": "extra wide egg noodles",
                                            "amount": 1.0,
                                            "unit": "lb"
                                        },
                                        {
                                            "recipeId": 39,
                                            "ingredientName": "Baking Powder",
                                            "amount": 0.25,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 39,
                                            "ingredientName": "Baking Soda",
                                            "amount": 0.25,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 39,
                                            "ingredientName": "Butter",
                                            "amount": 0.75,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 39,
                                            "ingredientName": "Cornstarch",
                                            "amount": 0.5,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 39,
                                            "ingredientName": "Egg",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 39,
                                            "ingredientName": "All-Purpose Flour",
                                            "amount": 1.5,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 39,
                                            "ingredientName": "pink food coloring (optional)",
                                            "amount": 1.0,
                                            "unit": "drop"
                                        },
                                        {
                                            "recipeId": 39,
                                            "ingredientName": "Pink Lemonade Kool-Aid",
                                            "amount": 0.5,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 39,
                                            "ingredientName": "Powdered Sugar",
                                            "amount": 0.25,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 39,
                                            "ingredientName": "Sugar",
                                            "amount": 1.25,
                                            "unit": "C"
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "Bay leaves",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "curry powder",
                                            "amount": 1.0,
                                            "unit": "Teaspoon"
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "garlic",
                                            "amount": 1.0,
                                            "unit": "Clove"
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "Cubes of Maggi",
                                            "amount": 3.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "Small bulb of Onion",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "dry pepper",
                                            "amount": 1.0,
                                            "unit": "Teaspoon"
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "Rice",
                                            "amount": 2.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "Medium sized Roma Tomatoes",
                                            "amount": 7.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "Salt",
                                            "amount": 2.0,
                                            "unit": "Teaspoons"
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "Scotch Bonnet Peppers",
                                            "amount": 3.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "Thyme",
                                            "amount": 1.0,
                                            "unit": "pinch"
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "Small can of Tomato puree",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "Vegetable Oil",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 40,
                                            "ingredientName": "water",
                                            "amount": 3.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 41,
                                            "ingredientName": "unsalted butter",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 41,
                                            "ingredientName": "sugar",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 41,
                                            "ingredientName": "eggs",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 41,
                                            "ingredientName": "vanilla extract",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 41,
                                            "ingredientName": "dark chocolate cocoa powder",
                                            "amount": 0.33,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 41,
                                            "ingredientName": "flour",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 41,
                                            "ingredientName": "baking powder",
                                            "amount": 0.25,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 41,
                                            "ingredientName": "a of salt",
                                            "amount": 1.0,
                                            "unit": "pinch"
                                        },
                                        {
                                            "recipeId": 41,
                                            "ingredientName": "Melted white chocolate, to decorate",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 41,
                                            "ingredientName": "candy pen and sprinkles, to decorate",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "egg",
                                            "amount": 1.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "milk",
                                            "amount": 1.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "yellow cornmeal",
                                            "amount": 0.33,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "chile powder",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "cayenne powder",
                                            "amount": 0.5,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "hot smoked paprika",
                                            "amount": 0.5,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "granulated garlic",
                                            "amount": 0.5,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "skinless catfish filets",
                                            "amount": 20.0,
                                            "unit": "oz"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "olive oil",
                                            "amount": 3.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "sea salt",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "freshly ground black pepper",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "light mayonnaise",
                                            "amount": 0.75,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "finely chopped dill pickle",
                                            "amount": 2.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "finely chopped jalapeno chile",
                                            "amount": 1.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "finely chopped scallion (white and green parts)",
                                            "amount": 1.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "dill pickle juice",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 42,
                                            "ingredientName": "fresh lemon juice",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 43,
                                            "ingredientName": "bacon",
                                            "amount": 6.0,
                                            "unit": "slices"
                                        },
                                        {
                                            "recipeId": 43,
                                            "ingredientName": "freshly ground black pepper",
                                            "amount": 4.0,
                                            "unit": "servings"
                                        },
                                        {
                                            "recipeId": 43,
                                            "ingredientName": "coarse salt",
                                            "amount": 4.0,
                                            "unit": "servings"
                                        },
                                        {
                                            "recipeId": 43,
                                            "ingredientName": "fresh sage",
                                            "amount": 10.0,
                                            "unit": "leaves"
                                        },
                                        {
                                            "recipeId": 43,
                                            "ingredientName": "garlic powder",
                                            "amount": 1.0,
                                            "unit": "pinch"
                                        },
                                        {
                                            "recipeId": 43,
                                            "ingredientName": "pork tenderloin",
                                            "amount": 2.0,
                                            "unit": "pounds"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "Pudding",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "avocados, ripe",
                                            "amount": 4.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "agave nectar",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "unsweetened cocoa powder",
                                            "amount": 0.66,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "chocolate almond milk",
                                            "amount": 6.0,
                                            "unit": "tbsp"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "vanilla",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "sea salt",
                                            "amount": 2.0,
                                            "unit": "pinches"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "fine espresso grounds",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "Chai Spice Blend",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "Chai Spice Blend",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "cinnamon",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "cardamom",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "ginger",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 44,
                                            "ingredientName": "nutmeg",
                                            "amount": 0.5,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 45,
                                            "ingredientName": "Brie Log such as Alouette",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 45,
                                            "ingredientName": "eggplant",
                                            "amount": 1.0,
                                            "unit": "small"
                                        },
                                        {
                                            "recipeId": 45,
                                            "ingredientName": "olive oil (for garnishing)",
                                            "amount": 4.0,
                                            "unit": "oz"
                                        },
                                        {
                                            "recipeId": 45,
                                            "ingredientName": "zucchini",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 45,
                                            "ingredientName": "yellow squash",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 45,
                                            "ingredientName": "ripe plum tomatoes",
                                            "amount": 2.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 45,
                                            "ingredientName": "thyme (chopped)",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "Bell Pepper",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "Bird's eye Chilli Pepper",
                                            "amount": 5.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "black pepper",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "Chicken Pieces",
                                            "amount": 8.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "red chilli powder",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "garlic",
                                            "amount": 5.0,
                                            "unit": "cloves"
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "Ginger",
                                            "amount": 0.5,
                                            "unit": "inch"
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "Seasoning Cube",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "Small sized Lemon (tablespoon all the juice out)",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "bulb of onion",
                                            "amount": 0.5,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "oregano",
                                            "amount": 1.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "paprika",
                                            "amount": 2.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "Red food colouring",
                                            "amount": 0.25,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "salt",
                                            "amount": 2.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "Scotch Bonnet Pepper (Ata Rodo)",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "Vegetable Oil",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 46,
                                            "ingredientName": "dark vinegar",
                                            "amount": 4.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "baking powder",
                                            "amount": 0.75,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "baking soda",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "freshly ground black pepper",
                                            "amount": 0.5,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "Cold Butter",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "buttermilk",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "coarsely grated Cheddar cheese",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "cottage cheese",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "chopped fresh dill",
                                            "amount": 1.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "shallot, chopped",
                                            "amount": 1.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "sugar",
                                            "amount": 1.0,
                                            "unit": "tablespoon"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "all-purpose flour",
                                            "amount": 2.25,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 47,
                                            "ingredientName": "whole wheat flour",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "beef steak",
                                            "amount": 400.0,
                                            "unit": "g"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "Butter",
                                            "amount": 2.0,
                                            "unit": "tablespoons"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "capers",
                                            "amount": 2.0,
                                            "unit": "Tbs"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "dry white wine",
                                            "amount": 0.75,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "flour",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "garlic, pressed",
                                            "amount": 2.0,
                                            "unit": "large cloves"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "ground black pepper",
                                            "amount": 0.25,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "lemon juice",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "Lemon wedges",
                                            "amount": 2.0,
                                            "unit": "servings"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "olive oil",
                                            "amount": 2.0,
                                            "unit": "Tbs"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "parsley, finely chopped",
                                            "amount": 2.0,
                                            "unit": "teaspoons"
                                        },
                                        {
                                            "recipeId": 48,
                                            "ingredientName": "salt",
                                            "amount": 0.75,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 49,
                                            "ingredientName": "Suya Spice",
                                            "amount": 1.5,
                                            "unit": "Tablespoons"
                                        },
                                        {
                                            "recipeId": 49,
                                            "ingredientName": "Chicken",
                                            "amount": 1.0,
                                            "unit": "pound"
                                        },
                                        {
                                            "recipeId": 49,
                                            "ingredientName": "chilli powder",
                                            "amount": 1.0,
                                            "unit": "teaspoon"
                                        },
                                        {
                                            "recipeId": 49,
                                            "ingredientName": "cooking spoon groundnut oil",
                                            "amount": 1.0,
                                            "unit": ""
                                        },
                                        {
                                            "recipeId": 49,
                                            "ingredientName": "Seasoning",
                                            "amount": 1.0,
                                            "unit": "cubes"
                                        },
                                        {
                                            "recipeId": 49,
                                            "ingredientName": "Onions and Tomatoes for Garnishing",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 49,
                                            "ingredientName": "Salt to taste",
                                            "amount": 1.0,
                                            "unit": "serving"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "bell peppers, chopped",
                                            "amount": 2.0,
                                            "unit": "medium"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "cayenne pepper",
                                            "amount": 3.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "green onions, chopped",
                                            "amount": 1.0,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "Oregano",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "pepper",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "red pepper",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "salt",
                                            "amount": 2.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "sausage, sliced",
                                            "amount": 1.0,
                                            "unit": "pound"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "boneless skinless chicken breasts (cut in 1 inch cubes)",
                                            "amount": 1.0,
                                            "unit": "pound"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "vegetable oil",
                                            "amount": 0.5,
                                            "unit": "cup"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "water",
                                            "amount": 6.0,
                                            "unit": "cups"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "white onions, chopped",
                                            "amount": 2.0,
                                            "unit": "large"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "white pepper",
                                            "amount": 1.0,
                                            "unit": "tsp"
                                        },
                                        {
                                            "recipeId": 50,
                                            "ingredientName": "white rice",
                                            "amount": 3.0,
                                            "unit": "cups"
                                        }
                                    ]
                                    )
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the locations table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_ingredients():
    db.session.execute('TRUNCATE ingredients;')
    db.session.commit()
