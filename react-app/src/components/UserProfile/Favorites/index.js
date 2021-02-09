import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink } from "react-router-dom";
import { fetchUserFavorites, deleteFavorite } from "../../../store/favorites";
import "./Favorites.css"

const FavoriteCards = ({ userFav, hidden, params }) => {
  const recipeId = userFav.id;
  const image = userFav.image;
  const title = userFav.title;

  const dispatch = useDispatch();

  const handleSubmit = async (e) => {
    e.preventDefault();
    dispatch(deleteFavorite(recipeId, params));
  };

  return (
    <>
      <div id="card">
        <div id="bar-info-container">
          <button id="unfavorite-button" hidden={hidden} onClick={handleSubmit}>
            Un-Favorite
          </button>
          <h4>{title}</h4>
        </div>

        <NavLink to={`/recipes/${recipeId}`}>
          <img alt="nope" src={image} />
        </NavLink>
      </div>
    </>
  );
};

const Favorites = ({ sessionUser, params }) => {

  const dispatch = useDispatch();

  const userFavorites = useSelector((state) => state.userFavorites);
  const intParams = parseInt(params);
  const sessId = sessionUser.id;

  useEffect(() => {
    dispatch(fetchUserFavorites(intParams))
  }, [dispatch]);

  return (
    <>
      <div id="favorite-container">
        <h4>My Favorites</h4>
        <div id="cards">
          {userFavorites &&
            userFavorites.map((userFav) => {
              return (
                <FavoriteCards
                  userFav={userFav}
                  params={params}
                  key={userFav.id}
                />
              );
            })}
        </div>
      </div>
    </>
  );
};

export default Favorites;
