import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  addFavorite,
  deleteFavorite,
} from "../../store/favorites";
import './Favorite.css'
import { setLoginModal, setTextModal } from "../../store/modal";

function Favorite({ recipeId, user }) {
  let [favoriteRecipe, setFavoriteRecipe] = useState(false);
  const dispatch = useDispatch();

  const handleFavoriteSubmit = async (e) => {
    e.preventDefault();

    if (user.id === null) {
      dispatch(setLoginModal(true));
    } else {
      dispatch(addFavorite(parseInt(recipeId), parseInt(user.id)));
      dispatch(setTextModal(true));
    }
  };

  const handleUnfavoriteSubmit = async (e) => {
    e.preventDefault();

    dispatch(deleteFavorite(parseInt(recipeId), parseInt(user.id)));
    dispatch(setTextModal(true));
  };

  return (
    <>
      <div id="favorite-div">
        {favoriteRecipe === true ? (
          <button id="favorite-me-button" onClick={handleUnfavoriteSubmit}>
            Unfavorite Me!
          </button>
        ) : (
          <button id="favorite-me-button" onClick={handleFavoriteSubmit}>
            Favorite Me!
          </button>
        )}
      </div>
    </>
  );
}

export default Favorite;
