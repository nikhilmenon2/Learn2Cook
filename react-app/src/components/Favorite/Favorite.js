import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  addFavorite,
  deleteFavorite,
} from "../../store/favorites";
import "./Favorite.css";
import { setLoginModal } from "../../store/modal";

function Favorite({ recipeId, user }) {
  let [favoriteRecipe, setFavoriteRecipe] = useState(false);
  const dispatch = useDispatch();

  const handleFavoriteSubmit = async (e) => {
    e.preventDefault();

    if (user.id === null) {
      dispatch(setLoginModal(true));
    } else {
      dispatch(addFavorite(parseInt(recipeId), parseInt(user.id)));
      setFavoriteRecipe(true);
    }
  };

  const handleUnfavoriteSubmit = async (e) => {
    e.preventDefault();
    dispatch(deleteFavorite(parseInt(recipeId), parseInt(user.id)));
    setFavoriteRecipe(false);
  };

  let session = useSelector((state) => state.session);

  useEffect(() => {
    if (user.id !== null) {
      if (session.user !== null) {
        const recipes = session.user.favoriteRecipe;
        const numOfrecipes = recipes.length;
        let i = 0;
        while (i < numOfrecipes) {
          if (recipes[i].id === parseInt(recipeId)) {
            setFavoriteRecipe(true);
            break;
          }
          i++;
        }
      }
    }
  }, [
    dispatch,
    favoriteRecipe,
    setFavoriteRecipe,
    addFavorite,
    deleteFavorite,
  ]);

  return (
    <>
      <div id="favorite-div">
        {favoriteRecipe === true ? (
          <button className="favorite-button" onClick={handleUnfavoriteSubmit}>
            Unfavorite
          </button>
        ) : (
          <button className="favorite-button" onClick={handleFavoriteSubmit}>
            Favorite
          </button>
        )}
      </div>
    </>
  );
}

export default Favorite;
