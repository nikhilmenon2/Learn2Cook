import React, { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { addFavorite, deleteFavorite, fetchUserFavorites } from "../../store/favorites"
import { setLoginModal, setTextModal } from '../../store/modal'

function Favorite ({recipeId, user}) {

  let [favoriteRecipe, setFavoriteRecipe] = useState(false);
  const dispatch = useDispatch();
  
  const handleFavoriteSubmit = async(e) => {
      e.preventDefault();

      if (user.id === null) {
        dispatch(setLoginModal(true))
      } else {
        dispatch(addFavorite(parseInt(recipeId), parseInt(user.id)))
        dispatch(setTextModal(true))

      }
  }

  const handleUnfavoriteSubmit = async(e) => {
      e.preventDefault();

      dispatch(deleteFavorite(parseInt(recipeId), parseInt(user.id)))
      dispatch(setTextModal(true))
  }

  let session = useSelector(state => state.session)

  useEffect( () => {
    if (user.id !== null) {
      if (session.user !== null) {
        const recipes = session.user.favoriteRecipes;
        const numOfrecipes = recipes.length;
        let i = 0;
          if (!recipes){
            return null;
            }
        
        while (i < numOfrecipes) {
          if (recipes[i].id === parseInt(recipeId)) {
            setFavoriteRecipe(true);
            break;
          }
          i++;
        }
      }

    }
  }, [dispatch, favoriteRecipe, setFavoriteRecipe, addFavorite, deleteFavorite])




  return (
    <>
      <div id='favorite-div'>
        { (favoriteRecipe === true) ? <h3>This Recipe Is One of Your Favorites!</h3> : <h3>Add To Your Favorites</h3> }
        { (favoriteRecipe === true) ? <button id='favorite-me-button' onClick={handleUnfavoriteSubmit}>Unfavorite Me!</button> : <button id='favorite-me-button' onClick={handleFavoriteSubmit}>Favorite Me!</button>}
      </div>
    </>
  );
}

export default Favorite;