import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink } from "react-router-dom";
import { fetchUserFavorites, deleteFavorite } from "../../../store/favorites";


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
            <h4>{title}</h4>
          <button id="unfavorite-button" hidden={hidden} onClick={handleSubmit}>
          Un-Favorite
        </button>
        </div>
        <NavLink to={`/recipes/${recipeId}`}>
          <img alt="nope" src={image} />
        </NavLink>
      </div>
    </>
  );
};

const Favorites = ({ sessionUser, params }) => {
  const [deleteHidden, setDeleteHidden] = useState(false);

  const dispatch = useDispatch();

  const userFavorites = useSelector((state) => state.userFavorites);
  const intParams = parseInt(params);
  const sessId = sessionUser.id;

  useEffect(() => {
    dispatch(fetchUserFavorites(params));

    if (sessId === intParams) {
      setDeleteHidden(false);
    } else {
      setDeleteHidden(true);
    }
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
                  hidden={deleteHidden}
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
