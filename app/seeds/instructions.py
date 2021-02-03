from app.models import db, Instruction


# Adds a demo location, you can add other locations here if you want

def seed_instructions():

    db.session.bulk_insert_mappings(Instruction,
                                    [
                                        {
                                            "recipeId": 1,
                                            "listOrder": 1,
                                            "specification": "Saut bacon in heavy gauge sauce pot until crispy"
                                        },
                                        {
                                            "recipeId": 1,
                                            "listOrder": 2,
                                            "specification": "Drain fat from sauce pot"
                                        },
                                        {
                                            "recipeId": 1,
                                            "listOrder": 3,
                                            "specification": "Add Tomato soup and vegetable stock and bring to a boil"
                                        },
                                        {
                                            "recipeId": 1,
                                            "listOrder": 4,
                                            "specification": "Add Alouette Sundried Tomato and Basil soft cheese"
                                        },
                                        {
                                            "recipeId": 1,
                                            "listOrder": 5,
                                            "specification": "Bring back to a boil and serve"
                                        },
                                        {
                                            "recipeId": 2,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 180 degrees Celsius (350 F) for a fan-forced oven or 200 degrees Celsius (392 F) for a convection oven."
                                        },
                                        {
                                            "recipeId": 2,
                                            "listOrder": 2,
                                            "specification": "Line a baking tray with baking paper."
                                        },
                                        {
                                            "recipeId": 2,
                                            "listOrder": 3,
                                            "specification": "Spray a thin layer of olive oil (any oil of your choice will do) on the baking paper. Set aside."
                                        },
                                        {
                                            "recipeId": 2,
                                            "listOrder": 4,
                                            "specification": "Crack and beat an egg on a plate. On a separate plate  add breadcrumbs."
                                        },
                                        {
                                            "recipeId": 2,
                                            "listOrder": 5,
                                            "specification": "Dip agnolotti in the beaten egg first."
                                        },
                                        {
                                            "recipeId": 2,
                                            "listOrder": 6,
                                            "specification": "Then coat it with breadcrumbs.  Repeat step 5 and 6 with the remaining agnolotti until egg and breadcrumbs are finished."
                                        },
                                        {
                                            "recipeId": 2,
                                            "listOrder": 7,
                                            "specification": "Place the crumbed agnolotti onto a baking tray. Once youve completed step 5 and 6, spray another thin layer of oil over the crumbed aganolotti."
                                        },
                                        {
                                            "recipeId": 2,
                                            "listOrder": 8,
                                            "specification": "Bake the crumbed agnolotti for 25 minutes or until golden brown."
                                        },
                                        {
                                            "recipeId": 2,
                                            "listOrder": 9,
                                            "specification": "Serve immediately with pasta sauce or ketchup."
                                        },
                                        {
                                            "recipeId": 3,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 35"
                                        },
                                        {
                                            "recipeId": 3,
                                            "listOrder": 2,
                                            "specification": "Mix onion, mayonnaise, parmigiano-reggiano, and parsley in a medium bowl. Season with salt and pepper."
                                        },
                                        {
                                            "recipeId": 3,
                                            "listOrder": 3,
                                            "specification": "Remove crusts from the bread. Using a 1\" round cookie cutter, cut bread into 32 rounds."
                                        },
                                        {
                                            "recipeId": 3,
                                            "listOrder": 4,
                                            "specification": "Place on a cookie sheet and bake, without turning, until golden, 1015 minutes."
                                        },
                                        {
                                            "recipeId": 3,
                                            "listOrder": 5,
                                            "specification": "Preheat broiler."
                                        },
                                        {
                                            "recipeId": 3,
                                            "listOrder": 6,
                                            "specification": "Spread about 1 tsp. onion mixture onto each round, then sprinkle with more parmigiano-reggiano and brown under broiler for 12 minutes."
                                        },
                                        {
                                            "recipeId": 3,
                                            "listOrder": 7,
                                            "specification": "Serve immediately."
                                        },
                                        {
                                            "recipeId": 4,
                                            "listOrder": 1,
                                            "specification": "In a skillet add olive oil, onions and bell pepper. Cook until tender, about 3  5 minutes."
                                        },
                                        {
                                            "recipeId": 4,
                                            "listOrder": 2,
                                            "specification": "Add tomatoes and seasonings, saute for 10 minutes."
                                        },
                                        {
                                            "recipeId": 4,
                                            "listOrder": 3,
                                            "specification": "Add black beans and cook until warm."
                                        },
                                        {
                                            "recipeId": 4,
                                            "listOrder": 4,
                                            "specification": "Serve with tortillas."
                                        },
                                        {
                                            "recipeId": 4,
                                            "listOrder": 5,
                                            "specification": "Additional toppings: Romaine"
                                        },
                                        {
                                            "recipeId": 4,
                                            "listOrder": 6,
                                            "specification": "Lettuce, Cheese, jalapenos, salsa, hot sauce, avocado, and greek yogurt"
                                        },
                                        {
                                            "recipeId": 5,
                                            "listOrder": 1,
                                            "specification": "Preheat your oven (*ding, this is a great toaster oven candidate) to 350F.  Line a rimmed baking sheet with aluminum foil."
                                        },
                                        {
                                            "recipeId": 5,
                                            "listOrder": 2,
                                            "specification": "Wash the endive and remove any unsightly outer leaves.  Slice each endive head in half from the stem to the tip.  Arrange the endive cut side up on the foil-lined baking sheet.  Coat the endive generously with olive oil."
                                        },
                                        {
                                            "recipeId": 5,
                                            "listOrder": 3,
                                            "specification": "Bake at 350F for 30 minutes, or until the outer edges are golden brown."
                                        },
                                        {
                                            "recipeId": 5,
                                            "listOrder": 4,
                                            "specification": "Meanwhile, fry the prosciutto in a skillet until crispy."
                                        },
                                        {
                                            "recipeId": 5,
                                            "listOrder": 5,
                                            "specification": "Drain onto paper towels, then crumble the prosciutto and set it aside."
                                        },
                                        {
                                            "recipeId": 5,
                                            "listOrder": 6,
                                            "specification": "When the endive is done roasting, arrange three pieces on a plate alongside a handful of sliced dried figs and pistachio nuts."
                                        },
                                        {
                                            "recipeId": 5,
                                            "listOrder": 7,
                                            "specification": "Drizzle a spoonful of honey over the plate, then sprinkle the endive with about 1/4th of the crumbled prosciutto."
                                        },
                                        {
                                            "recipeId": 6,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 425 degrees.Melt 1/2 of the butter and 1 tbsp brown sugar in a small skillet."
                                        },
                                        {
                                            "recipeId": 6,
                                            "listOrder": 2,
                                            "specification": "Brush onto on side of pizza crust."
                                        },
                                        {
                                            "recipeId": 6,
                                            "listOrder": 3,
                                            "specification": "Place on a baking sheet and bake for 3 minutes.Meanwhile, add the rest of butter and 1 tbsp brown sugar to the skillet again.Once it is melted add pecans and stir.Cook for 2-3 minutes over medium until pecans are toasted and coated in sugar."
                                        },
                                        {
                                            "recipeId": 6,
                                            "listOrder": 4,
                                            "specification": "Remove from heat.Take crust out of oven and spread pumpkin pie filling evenly on top."
                                        },
                                        {
                                            "recipeId": 6,
                                            "listOrder": 5,
                                            "specification": "Sprinkle with pumpkin pie spice."
                                        },
                                        {
                                            "recipeId": 6,
                                            "listOrder": 6,
                                            "specification": "Remove pecans from butter mixture and sprinkle evenly on top of pizza."
                                        },
                                        {
                                            "recipeId": 6,
                                            "listOrder": 7,
                                            "specification": "Bake for 7 more minutes.For Maple Whipped Cream: Using a cold bowl and beaters (I put mine in the freezer for about 30 minutes before using) beat heavy cream and maple syrup on high until stiff peaks form."
                                        },
                                        {
                                            "recipeId": 6,
                                            "listOrder": 8,
                                            "specification": "Remove pizza from oven."
                                        },
                                        {
                                            "recipeId": 6,
                                            "listOrder": 9,
                                            "specification": "Cut into 4 pieces. Top with a dollop or two of whipped cream and serve!"
                                        },
                                        {
                                            "recipeId": 7,
                                            "listOrder": 1,
                                            "specification": "First make the croutons: Preheat the oven Fan 160oC/180oC/Gas Mark"
                                        },
                                        {
                                            "recipeId": 7,
                                            "listOrder": 2,
                                            "specification": "Place a small roasting tray in the oven to heat up."
                                        },
                                        {
                                            "recipeId": 7,
                                            "listOrder": 3,
                                            "specification": "Cut the bread, crusts and all, into chunky crouton shapes."
                                        },
                                        {
                                            "recipeId": 8,
                                            "listOrder": 1,
                                            "specification": "Place the egg yolk, lemon, mustard and two sauces in a medium bowl."
                                        },
                                        {
                                            "recipeId": 8,
                                            "listOrder": 2,
                                            "specification": "Add plenty of salt and freshly ground black pepper and use a whisk to beat together.When nicely combined, gradually add the two oils, whisking between additions until a creamy, thick dressing forms. Check the seasoning and adjust to your taste.Break the lettuce into leaves, then thickly slice these."
                                        },
                                        {
                                            "recipeId": 8,
                                            "listOrder": 3,
                                            "specification": "Place in a bowl, add the croutons, half the cheese and half the dressing then mix well to coat the leaves."
                                        },
                                        {
                                            "recipeId": 8,
                                            "listOrder": 4,
                                            "specification": "Drizzle over the reaming dressing and scatter over the cheese."
                                        },
                                        {
                                            "recipeId": 8,
                                            "listOrder": 5,
                                            "specification": "Serve straight away."
                                        },
                                        {
                                            "recipeId": 9,
                                            "listOrder": 1,
                                            "specification": "Cut off the white part of the lemongrass stems, reserving tops."
                                        },
                                        {
                                            "recipeId": 9,
                                            "listOrder": 2,
                                            "specification": "Cut the white part into inch long pieces and flatten with the knife. Bring chicken stock to a boil in a large stockpot and add lemongrass stem and shrimp shells. Simmer for 2 minutes, then set aside to infuse."
                                        },
                                        {
                                            "recipeId": 9,
                                            "listOrder": 3,
                                            "specification": "Strain stock, then return to stock pot. Slice the remaining lemongrass stem and finely chop."
                                        },
                                        {
                                            "recipeId": 9,
                                            "listOrder": 4,
                                            "specification": "Add to stock along with shrimp, and simmer for 3-4 minutes until shrimp is pink."
                                        },
                                        {
                                            "recipeId": 9,
                                            "listOrder": 5,
                                            "specification": "Add lime juice, scallions, bean sprouts, carrots and daikon."
                                        },
                                        {
                                            "recipeId": 9,
                                            "listOrder": 6,
                                            "specification": "Stir well and season well."
                                        },
                                        {
                                            "recipeId": 9,
                                            "listOrder": 7,
                                            "specification": "Serve with a mint garnish."
                                        },
                                        {
                                            "recipeId": 10,
                                            "listOrder": 1,
                                            "specification": "Place first five items into a blender and pulse a few times."
                                        },
                                        {
                                            "recipeId": 10,
                                            "listOrder": 2,
                                            "specification": "Add the next berry and pulse 2-3 times. Repeat until all berries have been added, then blend on high until smooth."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 1,
                                            "specification": "Pre-heat the oven to 200 deg Celsius."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 2,
                                            "specification": "Lay a sheet of baking paper on a baking tray and grease it lightly with olive oil."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 3,
                                            "specification": "Lay the whole fish fillet on the baking sheet and rub the fish generously with the rest of the olive oil.Season with salt and pepper. I like to use Masterfoods Garlic Pepper whenever a recipe calls for salt and pepper."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 4,
                                            "specification": "Place the fish in an oven pre-heated to 200 deg Celsius for 15-20 minutes until fish is cooked. Do not overcook the fish. The standard, fan-forced or grill functions of the oven may be used.While the fish is cooking, lightly peel a piece of cucumber. About 150g large. Leave some skin on for a prettier appearance."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 5,
                                            "specification": "Cut the cucumber into strips and trim off the seeds. Retain the crunchy parts. Dice the cucumber strips. Set aside the cucumber dices in a bowl.Use only sun-dried tomatoes that are soaked in oil."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 6,
                                            "specification": "Remove the tomatoes from the jar and drain the excess oil."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 7,
                                            "specification": "Cut the tomatoes into small pieces."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 8,
                                            "specification": "Add the tomatoes to the cucumber.Stack 5 leaves of mint or basil together."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 9,
                                            "specification": "Roll up the stack of leaves. Using a pair of kitchen scissors, cut the herbs into fine strips."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 10,
                                            "specification": "Add them to the tomato mixture."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 11,
                                            "specification": "Add salt and pepper to taste, 1/2 teaspoon of sugar, 1 teaspoon of extra virgin olive oil, 1/2 teaspoon of balsamic vinegar and 1 teaspoon of toasted sesame seeds. Stir the tomato relish mixture well to combine."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 12,
                                            "specification": "Remove the fish from the oven."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 13,
                                            "specification": "Cut into servicing portions and place the relish on the top of the each fish fillet."
                                        },
                                        {
                                            "recipeId": 11,
                                            "listOrder": 14,
                                            "specification": "Garnish with sprigs of mint or basil."
                                        },
                                        {
                                            "recipeId": 12,
                                            "listOrder": 1,
                                            "specification": "To get started, place 1/4 cup of olive oil into a medium saucepan and allow to heat on medium heat. Once warm, place zucchini in pan and then sprinkle with garlic salt and cajun seasoning. Toss with tongs to get all of the zucchini coated with oil and seasoning. Cover with a lid and steam for two to three minutes."
                                        },
                                        {
                                            "recipeId": 12,
                                            "listOrder": 2,
                                            "specification": "Remove lid, toss zucchini noodles again and then cover for another 2 minutes."
                                        },
                                        {
                                            "recipeId": 12,
                                            "listOrder": 3,
                                            "specification": "Remove from heat.In the mean time, place the basil, garlic, and grated parmesan cheese into a food processor. Slowly add the olive oil, and then set to the side."
                                        },
                                        {
                                            "recipeId": 12,
                                            "listOrder": 4,
                                            "specification": "Add zucchini noodles, pesto, and chicken to a medium dish and toss until everything is fully coated."
                                        },
                                        {
                                            "recipeId": 12,
                                            "listOrder": 5,
                                            "specification": "Serve immediately."
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 1,
                                            "specification": "Blend cornflour and water until dissolved"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 2,
                                            "specification": "Add prawns, soy sauce, egg and sesame oil and mix well"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 3,
                                            "specification": "Combine honey & garlic sauce ingredients in a bowl and set aside"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 4,
                                            "specification": "Heat oil on high heat in a wok until the surface shimmers slightly"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 5,
                                            "specification": "Deep-fry half the prawns for 1 minute"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 6,
                                            "specification": "Remove with a slotted spoon and drain on kitchen paper"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 7,
                                            "specification": "Repeat with the rest of the prawns"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 8,
                                            "specification": "Drain the oil from the wok (you can save it for later in a jar)"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 9,
                                            "specification": "Wipe the wok clean with kitchen paper"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 10,
                                            "specification": "Heat the same wok to moderate heat and add the honey & garlic sauce ingredients"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 11,
                                            "specification": "Simmer for about 1  minutes"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 12,
                                            "specification": "Add the prawns till they are hot and just cooked through"
                                        },
                                        {
                                            "recipeId": 13,
                                            "listOrder": 13,
                                            "specification": "Garnish with spring onion and serve immediately."
                                        },
                                        {
                                            "recipeId": 14,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 400 degrees."
                                        },
                                        {
                                            "recipeId": 14,
                                            "listOrder": 2,
                                            "specification": "Salt and pepper chicken and place on parchment sheet."
                                        },
                                        {
                                            "recipeId": 14,
                                            "listOrder": 3,
                                            "specification": "Drizzle with olive oil."
                                        },
                                        {
                                            "recipeId": 14,
                                            "listOrder": 4,
                                            "specification": "Add onion, garlic, white wine, cherry tomatoes and basil. Wrap parchment tightly around contents and secure into a package with kitchen twine."
                                        },
                                        {
                                            "recipeId": 14,
                                            "listOrder": 5,
                                            "specification": "Place on cookie sheet."
                                        },
                                        {
                                            "recipeId": 14,
                                            "listOrder": 6,
                                            "specification": "Place in oven for 35 to 40 minutes or until thermometer inserted into chicken reads 165 degrees. Unwrap package and serve hot, with a garnish of fresh basil chiffonade."
                                        },
                                        {
                                            "recipeId": 15,
                                            "listOrder": 1,
                                            "specification": "Heat the oil in a deep-fryer or dutch oven to 365 degrees F."
                                        },
                                        {
                                            "recipeId": 15,
                                            "listOrder": 2,
                                            "specification": "Separate the onion slices into rings, and set aside. In a small bowl, stir together the flour, baking powder and salt."
                                        },
                                        {
                                            "recipeId": 15,
                                            "listOrder": 3,
                                            "specification": "Dip the onion slices into the flour mixture until they are all coated; set aside. This will help the batter adhere."
                                        },
                                        {
                                            "recipeId": 15,
                                            "listOrder": 4,
                                            "specification": "Gently beat the egg and buttermilk into the flour mixture using hand mixer."
                                        },
                                        {
                                            "recipeId": 15,
                                            "listOrder": 5,
                                            "specification": "Dip the floured rings into the batter to coat, then place on a wire rack to drain until the batter stops dripping. The wire rack may be placed over a sheet of aluminum foil for easier clean up."
                                        },
                                        {
                                            "recipeId": 15,
                                            "listOrder": 6,
                                            "specification": "Place the bread and panko crumbs out on a plate or shallow dish."
                                        },
                                        {
                                            "recipeId": 15,
                                            "listOrder": 7,
                                            "specification": "Place rings one at a time into the crumbs, and scoop the crumbs up over the ring to coat."
                                        },
                                        {
                                            "recipeId": 15,
                                            "listOrder": 8,
                                            "specification": "Give it a gentle tap as you remove it from the crumbs. The coating should cling very well. Repeat with remaining rings.I suggest completing this entire step before starting to fry rings. Its very easy to burn them if youre distracted. I may or may not be speaking from experience."
                                        },
                                        {
                                            "recipeId": 15,
                                            "listOrder": 9,
                                            "specification": "Deep fry the rings a few at a time for 2 to 3 minutes, or until golden brown. They should float to the top immediately  if they dont your oil is not hot enough. Turn rings over once during the frying time."
                                        },
                                        {
                                            "recipeId": 15,
                                            "listOrder": 10,
                                            "specification": "Remove form oil and transfer to a paper towel to drain. Season with seasoning salt, and serve warm."
                                        },
                                        {
                                            "recipeId": 16,
                                            "listOrder": 1,
                                            "specification": "Mix Sriracha Chili and Crema thoroughly until completely blended. Use more or less of the chili sauce depending on your heat preference."
                                        },
                                        {
                                            "recipeId": 17,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 350 degrees. Cover ham with a large piece of parchment and then foil."
                                        },
                                        {
                                            "recipeId": 17,
                                            "listOrder": 2,
                                            "specification": "Place ham, widest side down, on a heavy rimmed baking sheet."
                                        },
                                        {
                                            "recipeId": 17,
                                            "listOrder": 3,
                                            "specification": "Bake for 1 hour."
                                        },
                                        {
                                            "recipeId": 17,
                                            "listOrder": 4,
                                            "specification": "Heat glaze ingredients in a saucepan over medium heat until runny, about 5 minutes."
                                        },
                                        {
                                            "recipeId": 17,
                                            "listOrder": 5,
                                            "specification": "Remove ham from oven, and uncover. Score ham all over in a diamond pattern."
                                        },
                                        {
                                            "recipeId": 17,
                                            "listOrder": 6,
                                            "specification": "Brush 1/2 of the glaze over ham."
                                        },
                                        {
                                            "recipeId": 17,
                                            "listOrder": 7,
                                            "specification": "Increase temperature to 425 degrees."
                                        },
                                        {
                                            "recipeId": 17,
                                            "listOrder": 8,
                                            "specification": "Bake ham, uncovered, for 20 minutes."
                                        },
                                        {
                                            "recipeId": 17,
                                            "listOrder": 9,
                                            "specification": "Brush with remaining glaze, and bake until golden brown, 10 to 15 minutes more."
                                        },
                                        {
                                            "recipeId": 17,
                                            "listOrder": 10,
                                            "specification": "Let rest for 15 to 30 minutes before slicing."
                                        },
                                        {
                                            "recipeId": 18,
                                            "listOrder": 1,
                                            "specification": "Preheat the oven to 425Lightly grease a sheet pan with Olive oil."
                                        },
                                        {
                                            "recipeId": 18,
                                            "listOrder": 2,
                                            "specification": "Add chicken, egg, bread crumbs to a bowl and mix well.Stir in the cabbage, peppers, onions and carrot.It is best to just get right in with your hands and mix."
                                        },
                                        {
                                            "recipeId": 18,
                                            "listOrder": 3,
                                            "specification": "Roll into 2 balls, place on sheet pan."
                                        },
                                        {
                                            "recipeId": 18,
                                            "listOrder": 4,
                                            "specification": "Bake for 15-20 mins or until cooked through."
                                        },
                                        {
                                            "recipeId": 19,
                                            "listOrder": 1,
                                            "specification": "Heat oil in large saucepan over medium-high heat, add onion and cook for about 3 minutes."
                                        },
                                        {
                                            "recipeId": 19,
                                            "listOrder": 2,
                                            "specification": "Add celery, carrot and broccoli to pan and saut for about 5 minutes."
                                        },
                                        {
                                            "recipeId": 19,
                                            "listOrder": 3,
                                            "specification": "Add in all seasonings and cook additional 1 minute."
                                        },
                                        {
                                            "recipeId": 19,
                                            "listOrder": 4,
                                            "specification": "Add water, tomato paste, chickpeas and lentils, bring to a boil. Cover, reduce heat to low and simmer for 20 minutes.Meanwhile, cook couscous in separate pan according to package directions."
                                        },
                                        {
                                            "recipeId": 19,
                                            "listOrder": 5,
                                            "specification": "Add cilantro and lemon juice to stew and serve over warm couscous."
                                        },
                                        {
                                            "recipeId": 20,
                                            "listOrder": 1,
                                            "specification": "Start by pre-heating your oven to 350 degrees.  While the oven is pre-heating, heat the olive oil in a saut pan and add the shallot, diced mushroom, cranberry and thyme.  Saut for a few minutes until the shallot begins to wilt and then season with salt and pepper and set aside to cool."
                                        },
                                        {
                                            "recipeId": 20,
                                            "listOrder": 2,
                                            "specification": "Slice 12 pieces of brie and place each piece on the bread.  Follow with a spoonful of the cranberry, mushroom and shallot mixture and place on an oiled cookie sheet."
                                        },
                                        {
                                            "recipeId": 20,
                                            "listOrder": 3,
                                            "specification": "Bake the toasts for 15 minutes or just until the brie melts."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 1,
                                            "specification": "Dough:Note: If eggs are refrigerator cold, pour hot water over them and let stand for several minutes to warm before cracking."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 2,
                                            "specification": "Sprinkle the yeast over the warm water in a small cup or bowl, stir, and let stand for a minute of so to dissolve."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 3,
                                            "specification": "Combine the milk, sugar, salt, butter, and eggs in a large mixing bowl, and beat well. Stir in the dissolved yeast."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 4,
                                            "specification": "Add 2-1/2 cups of the flour, and beat until smooth and well blended."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 5,
                                            "specification": "Add 2-1/2 cups more flour and beat until the dough holds together in a rough, shaggy mass. Turn out onto a lightly floured surface and knead for a minute or two."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 6,
                                            "specification": "Let rest for 10 minutes.Resume kneading for 8 to 10 minutes more, gradually sprinkling on a little more flour if the dough sticks to your hands, until smooth and elastic."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 7,
                                            "specification": "Place in a greased bowl, cover with plastic wrap, and let rise in a warm place until double in bulk.Punch the risen dough down, and it is ready to be formed and baked according to other recipes which call for Sweet-"
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 8,
                                            "specification": "Roll Dough. You can also freeze the dough at this point, or store in the refrigerator for a few days in a tightly covered container.Apple"
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 9,
                                            "specification": "Mixture"
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 10,
                                            "specification": "In a fry pan add all the ingredients and cook for a few minutes until the apples just begin to soften. If there is a lot of syrup remove some of it otherwise it will leak out of the dough. Set aside.Assembly"
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 11,
                                            "specification": "Divide the dough in half."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 12,
                                            "specification": "Roll each half into a 14 x 9 rectangle."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 13,
                                            "specification": "Place on a piece of parchment."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 14,
                                            "specification": "Spread with half the cheese mixture lengthwise down center third of rectangle. Top with apple mixture. Make diagonal cuts from outer edges one half inch apart and 3 inches long. Fold alternate strips of dough over filling. Cover and let rise 45 minutes or until double in volume."
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 15,
                                            "specification": "Brush the dough with egg wash and sprinkle with sliced almonds"
                                        },
                                        {
                                            "recipeId": 21,
                                            "listOrder": 16,
                                            "specification": "Bake at 350 F. For 30 to 35 minutes."
                                        },
                                        {
                                            "recipeId": 22,
                                            "listOrder": 1,
                                            "specification": "Mix egg, oil, and milk on low speed of mixer for 1 minute."
                                        },
                                        {
                                            "recipeId": 22,
                                            "listOrder": 2,
                                            "specification": "Add Bette's"
                                        },
                                        {
                                            "recipeId": 22,
                                            "listOrder": 3,
                                            "specification": "Mix (or equivalent dry ingredients) and mix until smooth."
                                        },
                                        {
                                            "recipeId": 22,
                                            "listOrder": 4,
                                            "specification": "Put 1/2 cup all purpose gf flour in a shallow dish. Coat onion rings in flour."
                                        },
                                        {
                                            "recipeId": 22,
                                            "listOrder": 5,
                                            "specification": "Dip floured onions in prepared batter."
                                        },
                                        {
                                            "recipeId": 22,
                                            "listOrder": 6,
                                            "specification": "Fry in hot oil (375 degrees, at least 1-inch deep) until desired shade of brown."
                                        },
                                        {
                                            "recipeId": 23,
                                            "listOrder": 1,
                                            "specification": "Heat the oil in a 12-inch skillet over medium heat."
                                        },
                                        {
                                            "recipeId": 23,
                                            "listOrder": 2,
                                            "specification": "Add the rice and cook for 30 seconds, stirring constantly. Stir the broth, picante sauce and turmeric in the skillet and heat to a boil. Reduce the heat to low. Cover and cook for 15 minutes.Stir the kielbasa, shrimp and chicken in the skillet. Cover and cook for 5 minutes or until the rice is tender."
                                        },
                                        {
                                            "recipeId": 24,
                                            "listOrder": 1,
                                            "specification": "Combine the flour, coconut and salt in a large bowl."
                                        },
                                        {
                                            "recipeId": 24,
                                            "listOrder": 2,
                                            "specification": "In a smaller bowl, combine the vanilla and the can of sweetened condensed milk and mix well."
                                        },
                                        {
                                            "recipeId": 24,
                                            "listOrder": 3,
                                            "specification": "Add this goo to the dry ingredients and mix with a wooden spoon, or you could use your hands (sounds rather messy to me). I probably wouldn't use a mixer unless it's on a super low speed. This batter is going to be THICK."
                                        },
                                        {
                                            "recipeId": 24,
                                            "listOrder": 4,
                                            "specification": "Line baking sheets with parchment paper, and, using a big spoon or ice cream scooper, scoop the batter/dough onto the sheets."
                                        },
                                        {
                                            "recipeId": 24,
                                            "listOrder": 5,
                                            "specification": "In a preheated 350 degree oven, bake the macaroons for about 20 minutes, or until golden/toasty looking."
                                        },
                                        {
                                            "recipeId": 24,
                                            "listOrder": 6,
                                            "specification": "Drizzle some melted semi-sweet chocolate on top or use a chocolate/baker's chocolate mix and go for the dipped variety."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 1,
                                            "specification": "Soak dried navy beans overnight in a large pot. You want the water to be cold and about 2-3 inches above the beans. Cover and refrigerate at least 8 hours."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 2,
                                            "specification": "Drain and rinse the beans."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 3,
                                            "specification": "Place in a large pot and cover by 4-5 inches of fresh water. Bring to a boil, reduce heat and simmer for 1  1 hours until the beans are tender but not bursting."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 4,
                                            "specification": "In the meantime, combine teriyaki sauce, soy sauce, pineapple juice, brown sugar and ginger in a medium bowl."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 5,
                                            "specification": "Whisk until brown sugar has dissolved. Set aside."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 6,
                                            "specification": "Preheat oven to 350"
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 7,
                                            "specification": "Reserving 2 cups of the boiled water, drain the beans."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 8,
                                            "specification": "In a large Dutch oven, saut bacon for 3-4 minutes over medium high heat. With a slotted spoon remove bacon and set aside."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 9,
                                            "specification": "Add onions to the bacon fat and cook until translucent, about 5 minutes."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 10,
                                            "specification": "Add garlic and pineapple and saut for an additional minute, until the garlic becomes fragrant."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 11,
                                            "specification": "Place bacon back into the dutch oven and add the cubed ham steak, beans, reserved water, and prepared sauce. Stir well to combine."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 12,
                                            "specification": "Bake in the oven covered for 10 minutes. Reduce heat to 200 and continue to cook for 6 hours, stirring halfway through."
                                        },
                                        {
                                            "recipeId": 25,
                                            "listOrder": 13,
                                            "specification": "After 6 hours, remove lid, increase heat to 350 and cook for an additional 1-2 hours stirring every twenty minutes until the sauce has thickened."
                                        },
                                        {
                                            "recipeId": 26,
                                            "listOrder": 1,
                                            "specification": "Heat your oven up to 35"
                                        },
                                        {
                                            "recipeId": 26,
                                            "listOrder": 2,
                                            "specification": "Mix in a small bowl the soy sauce, worcestershire sauce, ketchup, vegetable oil, and lemon juice together. Rinse your pork chops, and place them in a glass baking dish."
                                        },
                                        {
                                            "recipeId": 26,
                                            "listOrder": 3,
                                            "specification": "Place half of your mixture over the top of the pork chops and bake for 30 minutes."
                                        },
                                        {
                                            "recipeId": 26,
                                            "listOrder": 4,
                                            "specification": "Remove from oven, turn over pork chops, and cover with the remaining mixture."
                                        },
                                        {
                                            "recipeId": 26,
                                            "listOrder": 5,
                                            "specification": "Bake for an additional 30 minutes.You are all done!"
                                        },
                                        {
                                            "recipeId": 26,
                                            "listOrder": 6,
                                            "specification": "Add a salad, mashed potatoes, and some bread!"
                                        },
                                        {
                                            "recipeId": 27,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 150C.In a pan, combine coconut oil, honey, lemon peel and lemon juice. Bring to boil. Take off the heat when the honey is dissolved."
                                        },
                                        {
                                            "recipeId": 27,
                                            "listOrder": 2,
                                            "specification": "Let cool a little.In another bowl, combine oats, flax seeds and chopped nuts."
                                        },
                                        {
                                            "recipeId": 27,
                                            "listOrder": 3,
                                            "specification": "Mix well."
                                        },
                                        {
                                            "recipeId": 27,
                                            "listOrder": 4,
                                            "specification": "Pour the honey mixture over the dry ingredients and stir until the oat mixture is well coated."
                                        },
                                        {
                                            "recipeId": 27,
                                            "listOrder": 5,
                                            "specification": "Spread the granola evenly on a baking pan, and bake for 20 minutes. Turn over the granola, and stir in the coconut flakes."
                                        },
                                        {
                                            "recipeId": 27,
                                            "listOrder": 6,
                                            "specification": "Bake for another 10 minutes."
                                        },
                                        {
                                            "recipeId": 27,
                                            "listOrder": 7,
                                            "specification": "Let cool and stir in the currants. Keep in airtight container."
                                        },
                                        {
                                            "recipeId": 28,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 400 degrees. Dip chicken in egg, then bread crumbs."
                                        },
                                        {
                                            "recipeId": 28,
                                            "listOrder": 2,
                                            "specification": "In 13 X 9 inch baking dish, arrange chicken. bake uncovered 20 minutes."
                                        },
                                        {
                                            "recipeId": 28,
                                            "listOrder": 3,
                                            "specification": "Pour pasta sauce over chicken, then top with cheese."
                                        },
                                        {
                                            "recipeId": 28,
                                            "listOrder": 4,
                                            "specification": "Bake 10 more minutes or until chicken reaches 170 degrees and is no longer pink."
                                        },
                                        {
                                            "recipeId": 28,
                                            "listOrder": 5,
                                            "specification": "Serve immediately with or over pasta."
                                        },
                                        {
                                            "recipeId": 29,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 350 F.Spray an 8x8 inch pan with cooking spray. Set aside.In a food processor, puree kidney beans and beets."
                                        },
                                        {
                                            "recipeId": 29,
                                            "listOrder": 2,
                                            "specification": "Transfer to a large bowl."
                                        },
                                        {
                                            "recipeId": 29,
                                            "listOrder": 3,
                                            "specification": "Add remaining ingredients and mix by hand until smooth and fully combined.Fold batter into the greased pan."
                                        },
                                        {
                                            "recipeId": 29,
                                            "listOrder": 4,
                                            "specification": "Bake for 35-40 minutes, turning the pan halfway through.When the brownies are done, test them with a toothpick. You want some batter to cling to the toothpick. Do not over bake."
                                        },
                                        {
                                            "recipeId": 29,
                                            "listOrder": 5,
                                            "specification": "Let cool completely. Refrigerate for one hour."
                                        },
                                        {
                                            "recipeId": 29,
                                            "listOrder": 6,
                                            "specification": "Cut into squares or use cookie cutters to make heart shapes."
                                        },
                                        {
                                            "recipeId": 30,
                                            "listOrder": 1,
                                            "specification": "In a blender add in the strawberries and sugar and blend until smooth. Set aside for a moment."
                                        },
                                        {
                                            "recipeId": 30,
                                            "listOrder": 2,
                                            "specification": "Pull out a bowl and add in the egg whites and powdered sugar."
                                        },
                                        {
                                            "recipeId": 30,
                                            "listOrder": 3,
                                            "specification": "Mix until it starts to form peaks."
                                        },
                                        {
                                            "recipeId": 30,
                                            "listOrder": 4,
                                            "specification": "Pour in the strawberry mixture and lemon juice mixing thoroughly."
                                        },
                                        {
                                            "recipeId": 30,
                                            "listOrder": 5,
                                            "specification": "Put the Guf in the freezer for about a half hour to firm completely, and then serve."
                                        },
                                        {
                                            "recipeId": 30,
                                            "listOrder": 6,
                                            "specification": "I have to say this is pretty close to the real thing."
                                        },
                                        {
                                            "recipeId": 31,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 325 degrees.  In a large bowl, cream together the butter and sugar.  Beat in eggs then stir in the cream, milk, liqueur, cinnamon, vanilla and bread.  Once well combined fold in the sliced bananas carefully."
                                        },
                                        {
                                            "recipeId": 31,
                                            "listOrder": 2,
                                            "specification": "Pour into a 13x9 baking dish and cook for 90 minutes or until completely set.  This can be served hot, room temp or cold. It can be topped with vanilla ice cream, whipped cream or as I did with the following topping."
                                        },
                                        {
                                            "recipeId": 31,
                                            "listOrder": 3,
                                            "specification": "In a sauce pan over medium high heat melt the butter then add the brown sugar.  Once melted add the banana slices and stir gently, cook until the syrup has reduced and the bananas have caramelized.  This will take about 5-10 minutes, be careful to not let your sugar burn. When ready ladle some of this hot sauce over each serving of bread pudding."
                                        },
                                        {
                                            "recipeId": 32,
                                            "listOrder": 1,
                                            "specification": "Heat the olive oil in a large pot over medium heat."
                                        },
                                        {
                                            "recipeId": 32,
                                            "listOrder": 2,
                                            "specification": "Add onions and saute until soft, or for about 5 minutes."
                                        },
                                        {
                                            "recipeId": 32,
                                            "listOrder": 3,
                                            "specification": "Add all other remaining ingredients and stir together. Increase the heat to medium high and bring to a boil. Cover and reduce heat to medium low so that the mixture simmers. Cook for 15-20 minutes, or until rice is fluffy and liquid is absorbed.*"
                                        },
                                        {
                                            "recipeId": 32,
                                            "listOrder": 4,
                                            "specification": "Serve with salsa, cheese, and sour cream."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 1,
                                            "specification": "Slice mushrooms and pound chicken breast with a mallet between 2 sheets of wax paper to about 1/4 inch. Dredge breast in seasoned crumbs."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 2,
                                            "specification": "Heat a heavy stainless or cast iron pan (don't use non-stick)."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 3,
                                            "specification": "Add the butter and the olive oil till butter melts and is bubbly."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 4,
                                            "specification": "Add chicken breast and brown on both sides."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 5,
                                            "specification": "Remove browned breast."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 6,
                                            "specification": "Add additional olive oil and saute mushrooms and garlic."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 7,
                                            "specification": "Deglaze pan with wine."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 8,
                                            "specification": "Add browned chicken breast back to pan. Bring to boil, reduce heat, cover and simmer for 30 min."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 9,
                                            "specification": "Remove chicken from pan."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 10,
                                            "specification": "Add cream and reduce sauce 50%."
                                        },
                                        {
                                            "recipeId": 33,
                                            "listOrder": 11,
                                            "specification": "Serve over cooked pasta, if desired."
                                        },
                                        {
                                            "recipeId": 34,
                                            "listOrder": 1,
                                            "specification": "In a bowl, season the chopped chicken breast with one seasoning cube, ginger powder, black pepper, chili powder, and garlic and set aside."
                                        },
                                        {
                                            "recipeId": 34,
                                            "listOrder": 2,
                                            "specification": "Whisk your eggs and set aside.Season your breadcrumbs with the seasoning cubes and divide into 2 equal portions and set aside.In a blender or food processor, pour in your chicken breast, flour, 1 portion of breadcrumbs, and egg and blend till smooth."
                                        },
                                        {
                                            "recipeId": 34,
                                            "listOrder": 3,
                                            "specification": "Scrape into a bowl and mold into little balls using the extra breadcrumbs to properly coat it. The smaller the balls the better as the chicken would cook through better.In a deep fryer or a huge pot of oil on medium heat, allow to heat but not be extra hot and dunk your popcorn chicken to fry till brown."
                                        },
                                        {
                                            "recipeId": 34,
                                            "listOrder": 4,
                                            "specification": "Serve hot."
                                        },
                                        {
                                            "recipeId": 35,
                                            "listOrder": 1,
                                            "specification": "Heat the oil in a pan. Grate the onion and the garlic into it."
                                        },
                                        {
                                            "recipeId": 35,
                                            "listOrder": 2,
                                            "specification": "Add the grated ginger as well."
                                        },
                                        {
                                            "recipeId": 35,
                                            "listOrder": 3,
                                            "specification": "Let it saut for 2 mins."
                                        },
                                        {
                                            "recipeId": 35,
                                            "listOrder": 4,
                                            "specification": "Add in the turmeric powder, coriander powder, cumin powder and kashmiri mirch and saut for a couple more minutes."
                                        },
                                        {
                                            "recipeId": 35,
                                            "listOrder": 5,
                                            "specification": "Add the kasuri methi and the tomato paste mixed in water."
                                        },
                                        {
                                            "recipeId": 35,
                                            "listOrder": 6,
                                            "specification": "Add some more water if required."
                                        },
                                        {
                                            "recipeId": 35,
                                            "listOrder": 7,
                                            "specification": "When it starts to boil, add the salt and paneer cubes."
                                        },
                                        {
                                            "recipeId": 35,
                                            "listOrder": 8,
                                            "specification": "Let it cook in the gravy for a couple of minutes."
                                        },
                                        {
                                            "recipeId": 35,
                                            "listOrder": 9,
                                            "specification": "Add the cream and sugar and mix well. Dont let it boil after you have added the cream, just simmer for 15 minutes or so."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 1,
                                            "specification": "How to Make Strawberry Creme Cheese Filling"
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 2,
                                            "specification": "Add cream cheese, strawberries, vanilla extract, lemon juice, and granulated sugar into a medium-sized mixing bowl."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 3,
                                            "specification": "Use a hand mixer, wooden spoon, or spatula to mix ingredients."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 4,
                                            "specification": "Mix until smooth."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 5,
                                            "specification": "Set aside."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 6,
                                            "specification": "How to Blend Chocolate Crepes Ingredients"
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 7,
                                            "specification": "Combine flour, sugar, cocoa powder, salt, and eggs to a food processor or blender."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 8,
                                            "specification": "If using a food processor, keep it running as you add milk and water. Continue to pulse intil blended well."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 9,
                                            "specification": "Pour in melted butter and vanilla extract."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 10,
                                            "specification": "Set bowl aside."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 11,
                                            "specification": "How to Make Chocolate Crepes"
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 12,
                                            "specification": "Heat crepe pan or 8\"-10\" omelet pan over medium heat."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 13,
                                            "specification": "Pour 1/4 cup of batter directly into the middle of the pan and swirl to cover the bottom."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 14,
                                            "specification": "Cook the crepe for 2-3 minutes or until the bottom is light brown and the edges are completely set."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 15,
                                            "specification": "Flip the crepe over and cook for an additional minute."
                                        },
                                        {
                                            "recipeId": 36,
                                            "listOrder": 16,
                                            "specification": "Transfer to a serving platter and repeat for the rest of the batter."
                                        },
                                        {
                                            "recipeId": 37,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 375 degrees. Spray a large 2 large casserole dish with cooking spray.Three separate items need cooked. You can cook them all at once to avoid having one sit aside for too long.(Prepare your potatoes and set aside) Meanwhile, boil your noodles but reduce cooking time by 4 minutes to avoid overcooking."
                                        },
                                        {
                                            "recipeId": 37,
                                            "listOrder": 2,
                                            "specification": "Drain and set aside. Prepare your onions by cooking in the 4 tbsp. of butter over medium heat until tender."
                                        },
                                        {
                                            "recipeId": 37,
                                            "listOrder": 3,
                                            "specification": "Add milk, 1 cup of cheese, salt and pepper, and onion mixture to your potatoes. Mash using a large wooden spoon or a hand held potato masher. Mash until soft, but some chunks remain. You don't want a completely smooth texture."
                                        },
                                        {
                                            "recipeId": 37,
                                            "listOrder": 4,
                                            "specification": "Add in your noodles and toss to coat. Taste for seasoning and add more if necessary. If mixture seems dry, add more milk and butter until the entire mixture is lightly coated."
                                        },
                                        {
                                            "recipeId": 37,
                                            "listOrder": 5,
                                            "specification": "Place in casserole dish."
                                        },
                                        {
                                            "recipeId": 37,
                                            "listOrder": 6,
                                            "specification": "Sprinkle with the remaining \u00bd cup of cheese."
                                        },
                                        {
                                            "recipeId": 37,
                                            "listOrder": 7,
                                            "specification": "Bake in your preheated oven for 25 minutes or until cheese starts to bubble."
                                        },
                                        {
                                            "recipeId": 37,
                                            "listOrder": 8,
                                            "specification": "Serve immediately and enjoy!"
                                        },
                                        {
                                            "recipeId": 38,
                                            "listOrder": 1,
                                            "specification": "Prepare a cookie sheet by greasing with non-stick cooking spray. Preheat oven to 35"
                                        },
                                        {
                                            "recipeId": 38,
                                            "listOrder": 2,
                                            "specification": "Cream butter and sugar together in your mixer, scraping the sides of your bowl."
                                        },
                                        {
                                            "recipeId": 38,
                                            "listOrder": 3,
                                            "specification": "Add your egg and mix well."
                                        },
                                        {
                                            "recipeId": 38,
                                            "listOrder": 4,
                                            "specification": "Mix in baking powder, baking soda, Kool-Aid and cornstarch. Once its well mixed (the Kool-Aid will be mixed once it turns your dough pink), add a drop of pink food coloring, if more color is desired. Next, start adding your flour a half cup at a time until its all added."
                                        },
                                        {
                                            "recipeId": 38,
                                            "listOrder": 5,
                                            "specification": "Roll the dough into walnut-sized balls and roll in the powder sugar, giving them a light coating."
                                        },
                                        {
                                            "recipeId": 38,
                                            "listOrder": 6,
                                            "specification": "Place 2 apart on a room-temp baking sheet (let your sheet cool in between batches if you are reusing the same one)."
                                        },
                                        {
                                            "recipeId": 38,
                                            "listOrder": 7,
                                            "specification": "Bake in the oven 9-10 minutes, they wont brown too much, so watch them closely. Over-baking will make them hard and crunchy!"
                                        },
                                        {
                                            "recipeId": 39,
                                            "listOrder": 1,
                                            "specification": "*Wash rice by rubbing the rice between your palms in a bowl of water and draining the water till clear.Blend tomatoes, pepper and garlic and bring to boil till the excess water dries up.Chop Onions"
                                        },
                                        {
                                            "recipeId": 39,
                                            "listOrder": 2,
                                            "specification": "Heat up vegetable oil and pour in chopped onions and fry."
                                        },
                                        {
                                            "recipeId": 39,
                                            "listOrder": 3,
                                            "specification": "Pour in the can of tomato puree and fry."
                                        },
                                        {
                                            "recipeId": 39,
                                            "listOrder": 4,
                                            "specification": "Pour in blended tomato and pepper mix into the pot and stir in."
                                        },
                                        {
                                            "recipeId": 39,
                                            "listOrder": 5,
                                            "specification": "Pour in salt, dry pepper, curry, thyme, bay leaves and maggi cubes.Allow it to simmer on low heat for 3 minutes.Reduce the heat to the lowest level and pour in the washed rice."
                                        },
                                        {
                                            "recipeId": 39,
                                            "listOrder": 6,
                                            "specification": "Pour in the water and stir and leave on low heat for 20 minutes or till the rice is soft.Tip: To get the party rice flavor, increase the heat on the rice and burn the bottom of the pot with the pot covered and stir the rice after 3 minutes of burning.Stir the rice and serve with any protein of your choice.\u00a0 // <![CDATA[(adsbygoogle = window.adsbygoogle || []).push({});// ]]&gt;A video I shared on Instagram recently"
                                        },
                                        {
                                            "recipeId": 40,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 350 degrees F. Spray the Coffin Cake Pan with baking spray."
                                        },
                                        {
                                            "recipeId": 40,
                                            "listOrder": 2,
                                            "specification": "Melt 1/2 cup butter in a microwave safe bowl. In a large mixing bowl mix together the melted butter and sugar. When smooth, add the eggs and vanilla extract and mix well."
                                        },
                                        {
                                            "recipeId": 40,
                                            "listOrder": 3,
                                            "specification": "Beat in the dark chocolate cocoa powder. When smooth, beat in flour, salt, and baking powder."
                                        },
                                        {
                                            "recipeId": 40,
                                            "listOrder": 4,
                                            "specification": "Fill the coffins about 2/3 of the way with the brownie batter."
                                        },
                                        {
                                            "recipeId": 40,
                                            "listOrder": 5,
                                            "specification": "Bake at 350 degrees F for 20 to 25 minutes (22 minutes worked for me)."
                                        },
                                        {
                                            "recipeId": 40,
                                            "listOrder": 6,
                                            "specification": "When the brownies have cooled, decorate as you like."
                                        },
                                        {
                                            "recipeId": 41,
                                            "listOrder": 1,
                                            "specification": "Whisk the egg and milk in a medium bowl."
                                        },
                                        {
                                            "recipeId": 41,
                                            "listOrder": 2,
                                            "specification": "Combine the cornmeal, chile powder, cayenne powder, paprika, and garlic in a large zip-top bag."
                                        },
                                        {
                                            "recipeId": 41,
                                            "listOrder": 3,
                                            "specification": "Dip each catfish filet in the egg mixture."
                                        },
                                        {
                                            "recipeId": 41,
                                            "listOrder": 4,
                                            "specification": "Let excess egg drip off and place the filets in the bag with the cornmeal mixture. Zip the top and shake the bag until all pieces are well coated."
                                        },
                                        {
                                            "recipeId": 41,
                                            "listOrder": 5,
                                            "specification": "Remove the filets and lay side by side on a plate (do not overlap)."
                                        },
                                        {
                                            "recipeId": 41,
                                            "listOrder": 6,
                                            "specification": "Place in the refrigerator for 30 minutes. (Refrigeration helps keep the crust adhered during cooking.)"
                                        },
                                        {
                                            "recipeId": 41,
                                            "listOrder": 7,
                                            "specification": "While the fish chills, make the sauce."
                                        },
                                        {
                                            "recipeId": 41,
                                            "listOrder": 8,
                                            "specification": "Whisk the first 6 ingredients (through lemon juice) in a small bowl. Season with salt and pepper and set aside."
                                        },
                                        {
                                            "recipeId": 41,
                                            "listOrder": 9,
                                            "specification": "Heat a large, nonstick skillet over medium heat and add the olive oil. When the oil is hot (but not smoking), season the catfish filets with salt and pepper and add to the skillet. Fry until crispy on the outside and tender on the inside, 3-4 minutes per side, depending on thickness."
                                        },
                                        {
                                            "recipeId": 41,
                                            "listOrder": 10,
                                            "specification": "Divide the fish among 4 plates and top each with a dollop of tartar sauce or pass the sauce at the table."
                                        },
                                        {
                                            "recipeId": 42,
                                            "listOrder": 1,
                                            "specification": "Remove about an inch off the tapered end of each tenderloin to make a perfect cylinder.Season with salt, pepper, and a pinch of garlic powder."
                                        },
                                        {
                                            "recipeId": 42,
                                            "listOrder": 2,
                                            "specification": "Lay the bacon strips in a overlapping line on a sheet of cling wrap."
                                        },
                                        {
                                            "recipeId": 42,
                                            "listOrder": 3,
                                            "specification": "Place sage leaves all over bacon (about 9-10 leaves)."
                                        },
                                        {
                                            "recipeId": 42,
                                            "listOrder": 4,
                                            "specification": "Place 1 piece of tenderloin across the short ends of the bacon and roll to cover with the bacon.Repeat with the other tenderloin segments.Preheat oven to 425 F."
                                        },
                                        {
                                            "recipeId": 42,
                                            "listOrder": 5,
                                            "specification": "Place the tenderloin in non-stick pan and sear on all sides over medium-high heat."
                                        },
                                        {
                                            "recipeId": 42,
                                            "listOrder": 6,
                                            "specification": "Transfer the pan to the preheated oven and cook for 8-10 minutes, turning the pieces after 5 minutes to ensure even cooking."
                                        },
                                        {
                                            "recipeId": 43,
                                            "listOrder": 1,
                                            "specification": "Scoop the avocado into a food processor or blender. Measure in the agave nectar, cocoa powder, almond milk, vanilla and sea salt. Pulse and blend until silky smooth, scraping down sides as needed."
                                        },
                                        {
                                            "recipeId": 43,
                                            "listOrder": 2,
                                            "specification": "Scrape into a large bowl and stir in the espresso grounds and chai spice mix. Taste and adjust espresso and chai flavoring as desired."
                                        },
                                        {
                                            "recipeId": 43,
                                            "listOrder": 3,
                                            "specification": "Scoop into smaller ramekins, cover with plastic wrap and refrigerate for 30 minutes or overnight to set."
                                        },
                                        {
                                            "recipeId": 43,
                                            "listOrder": 4,
                                            "specification": "Notes"
                                        },
                                        {
                                            "recipeId": 43,
                                            "listOrder": 5,
                                            "specification": "* Agave Nectar can be substituted with maple syrup. If you do this, you may need to decrease the amount of almond milk you use to keep the pudding thick."
                                        },
                                        {
                                            "recipeId": 44,
                                            "listOrder": 1,
                                            "specification": "Remove outer peel from eggplant and dice into  inch pieces"
                                        },
                                        {
                                            "recipeId": 44,
                                            "listOrder": 2,
                                            "specification": "Heat 1-2 oz. of olive oil in a heavy gauge skillet"
                                        },
                                        {
                                            "recipeId": 44,
                                            "listOrder": 3,
                                            "specification": "Saut the diced eggplant for 2-3 minutes then place on a towel to drain"
                                        },
                                        {
                                            "recipeId": 44,
                                            "listOrder": 4,
                                            "specification": "After draining place cooked eggplant into a small oval casserole dish"
                                        },
                                        {
                                            "recipeId": 44,
                                            "listOrder": 5,
                                            "specification": "Preheat oven to 375 F"
                                        },
                                        {
                                            "recipeId": 44,
                                            "listOrder": 6,
                                            "specification": "Carefully slice the zucchini , yellow squash , and tomatoes about  inch even slices"
                                        },
                                        {
                                            "recipeId": 44,
                                            "listOrder": 7,
                                            "specification": "Slice the Brie also into  inch slices (utilizing a cheese wire makes simplifies this)"
                                        },
                                        {
                                            "recipeId": 44,
                                            "listOrder": 8,
                                            "specification": "Begin placing sliced yellow squash , zucchini , sliced Brie and tomatoes in a shingled pattern working from the outside of the casserole towards the center"
                                        },
                                        {
                                            "recipeId": 44,
                                            "listOrder": 9,
                                            "specification": "When all vegetables and cheese are placed in the casserole, drizzle with the remaining olive oil and sprinkle with chopped thyme"
                                        },
                                        {
                                            "recipeId": 44,
                                            "listOrder": 10,
                                            "specification": "Season with salt and pepper and bake in the oven for 10-15 minutes until bubbly"
                                        },
                                        {
                                            "recipeId": 45,
                                            "listOrder": 1,
                                            "specification": "Wash the Chicken and set aside.Blend all the Ingredients together and pour as needed on the chicken. Rub it into the chicken and allow to marinate for about 3-5 hours.If you have a grill, heat up the grill and and place chicken on to cook. If you don\u2019t and you are using an oven, set the oven to grill/broil at first and let the chicken brown on both sides then reset the oven to bake at 370 F and bake the chicken till cooked.If there is left over sauce from the blend, heat it up with a little water and serve with the peri peri chicken. Savoury Rice"
                                        },
                                        {
                                            "recipeId": 45,
                                            "listOrder": 2,
                                            "specification": "Ingredients2 cups of Rice1/2 bulb of Onion1/4 pound of Cabbage1 cup of chopped carrots1 egg1 cup of melted butter"
                                        },
                                        {
                                            "recipeId": 45,
                                            "listOrder": 3,
                                            "specification": "Chicken Seasoning1 teaspoon of currya pinch of thyme Wash and Parboil the Rice for 10 minutes."
                                        },
                                        {
                                            "recipeId": 45,
                                            "listOrder": 4,
                                            "specification": "Heat the butter in a pot and pour in the chopped onions, carrots and cabbage and stir in.Break the egg into the veggie mix and stir in."
                                        },
                                        {
                                            "recipeId": 45,
                                            "listOrder": 5,
                                            "specification": "Add your seasoning and pour in the parboiled rice."
                                        },
                                        {
                                            "recipeId": 45,
                                            "listOrder": 6,
                                            "specification": "Pour in 1 cup of water and cook on medium heat till the rice is soft. Stir and serve with the chicken."
                                        },
                                        {
                                            "recipeId": 46,
                                            "listOrder": 1,
                                            "specification": "Preheat oven to 375F with the rack in middle position.Make the Scone"
                                        },
                                        {
                                            "recipeId": 47,
                                            "listOrder": 1,
                                            "specification": "Place half the butter and half the dry ingredients in the bowl. Pulse until the butter is reduced to pea-sized pieces, with dough still dry."
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 1,
                                            "specification": "Place all the ingredients in a large bowl and use a pastry cutter to incorporate the butter into the dough."
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 2,
                                            "specification": "Cut by pressing on butter, then gathering flour onto it in two quick strokes."
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 3,
                                            "specification": "Cut until butter slices become pea-sized.Dont over process or mix. Dough will be dry. Break large lumps of butter by hand, and toss dry dough with your fingers.Blend the cheeses, dill, shallot and pepper with the Scone"
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 4,
                                            "specification": "Mix using a wooden spoon."
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 5,
                                            "specification": "Drizzle the buttermilk over the dough and drop the cottage cheese in the middle, and stir until mixed."
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 6,
                                            "specification": "Add more buttermilk if dough is too dry to hold together."
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 7,
                                            "specification": "Place dough on a lightly floured surface and divide into two. Form 2 discs and flatten each to a thickness of about 1-1/2 inches, cut into 6 wedges for a total of 1"
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 8,
                                            "specification": "Arrange an inch apart on a cookie sheet."
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 9,
                                            "specification": "Bake for 15 minutes, rotate the pan, and bake another 10 to 15 minutes, until scones are light brown on top and darker at the bottom. Bread should no longer be soft and doughy in the center."
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 10,
                                            "specification": "Bake in 2 batches if scones dont fit in one cookie sheet."
                                        },
                                        {
                                            "recipeId": 48,
                                            "listOrder": 11,
                                            "specification": "Serve warm or cool in a wire rack before wrapping in foil or plastic wrap/bag. Freshly baked scones can be kept at room temperature for up to 2 days, and in the refrigerator for a week."
                                        },
                                        {
                                            "recipeId": 49,
                                            "listOrder": 1,
                                            "specification": "Flatten the steaks lightly with a meat mallet."
                                        },
                                        {
                                            "recipeId": 49,
                                            "listOrder": 2,
                                            "specification": "Combine flour, salt and pepper, dip steaks into the mixture, coating both sides.Saut the steaks in a hot mixture of butter and olive oil over medium heat, about 4 minutes on each side."
                                        },
                                        {
                                            "recipeId": 49,
                                            "listOrder": 3,
                                            "specification": "Remove from the pan and set aside.Saut the garlic in the same fat for about 1 minute, stirring."
                                        },
                                        {
                                            "recipeId": 49,
                                            "listOrder": 4,
                                            "specification": "Add the wine and lemon juice, stir and simmer for 5 minutes to slightly reduce the liquid."
                                        },
                                        {
                                            "recipeId": 49,
                                            "listOrder": 5,
                                            "specification": "Add capers, stir. Return the steaks to the pan, cover and simmer over low heat for 4 minutes."
                                        },
                                        {
                                            "recipeId": 50,
                                            "listOrder": 1,
                                            "specification": "Heat the oven to 500 F.Wash and season the chicken with the Suya spice, chilli powder, seasoning cubes, salt and drizzle the oil over it."
                                        },
                                        {
                                            "recipeId": 50,
                                            "listOrder": 2,
                                            "specification": "Place the chicken in the oven and grill for 40 minutes. Check the chicken occasionally and flip on both sides so it can cook properly."
                                        },
                                        {
                                            "recipeId": 50,
                                            "listOrder": 3,
                                            "specification": "Serve hot garnished with the onions and tomato and a bit of suya spice sprinkled over the chicken."
                                        },
                                        
                                    ]
                                    )
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the locations table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_instructions():
    db.session.execute('TRUNCATE instructions;')
    db.session.commit()
