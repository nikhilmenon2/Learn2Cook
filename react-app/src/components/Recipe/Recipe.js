import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import {recipesDataDisplay} from "../../store/recipes"
import { useParams } from 'react-router-dom'


function Recipe() {
    const dispatch = useDispatch()
    let results = useSelector(state => state.recipes.recipesdata)
    const {recipeId}  = useParams();


      useEffect(() => {
        (async () => {
            await dispatch(recipesDataDisplay(recipeId))
        })();
    }, [dispatch, recipeId])

    return (
        <div>
           {results} 
        </div>
    )
}

export default Recipe
