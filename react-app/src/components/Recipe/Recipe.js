import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import {recipesDataDisplay} from "../../store/recipes"
import { useParams } from 'react-router-dom'


function Recipe() {
    const dispatch = useDispatch()
   
   
    let recipe = useSelector(state => state.recipes.recipe)
    let ingredients = useSelector(state => state.recipes.ingredients)

    const {recipeId}  = useParams();

   console.log(recipe)
   
    
      useEffect(() => {
        ( () => {
             dispatch(recipesDataDisplay(recipeId))
        })();
    }, [dispatch, recipeId])

    if (!recipe && !ingredients){
        return null;
    }

    return (
        <div>
        <h1>{recipe.title}</h1>
       <h1>{recipe.description}</h1>
       
        </div>
    )
}

export default Recipe
