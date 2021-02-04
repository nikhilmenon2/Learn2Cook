import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import {recipesDataDisplay} from "../../store/recipes"
import { useParams } from 'react-router-dom'


function Recipe() {
    const dispatch = useDispatch()
    let recipe = useSelector(state => state.recipes.recipe)
    let ingredients = useSelector(state => state.recipes.ingredients)
    let instructions = useSelector(state => state.recipes.instructions)
    let reviews = useSelector(state => state.recipes.review)
    let users = useSelector(state => state.recipes.users)

    const {recipeId}  = useParams();
      useEffect(() => {
        ( () => {
             dispatch(recipesDataDisplay(recipeId))
        })();
    }, [dispatch, recipeId])

    if (!recipe && !ingredients &&!instructions && !reviews && !users ){
        return null;
    }

 

    return (
        <div>
        <h1>{recipe.title}</h1>
       <h3>{recipe.description}</h3>
       <img src={recipe.image}></img>
       <ul>
           <h3>Ingredients</h3>
            {ingredients.map(ingredient => 
               <div>{ingredient.amount} {ingredient.unit} {ingredient.ingredientName} </div> 
            )}
       </ul>
        <ul>
           <h3>Instructions</h3>
            {instructions.map(instructions=> 
               <div>{instructions.listOrder} {instructions.specification}  </div> 
            )}
       </ul>
       <div>
            <h3>Reviews</h3>
                {reviews.map(review=> 
               <div>{review.review} -
                 </div> 
            )}
            {/* {users.map(user =>
               <div> {user.firstName} </div>
                )} */}
       </div>
        </div>
    )
}

export default Recipe
