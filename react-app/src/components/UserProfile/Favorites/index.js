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
        <button id="unfavorite-button" hidden={hidden} onClick={handleSubmit}>
          unfavorite
        </button>
        <NavLink to={`/recipes/${recipeId}`}>
          <img alt="nope" src={image} />
          <div id="bar-info-container">
            <h4>{title}</h4>
          </div>
        </NavLink>
      </div>
    </>
  );
};

const Favorites = ({ sessionUser, params }) => {
  const [deleteHidden, setDeleteHidden] = useState(false);

  const dispatch = useDispatch();

  const userFavorites = useSelector((state) => state.session.user.favoriteRecipe);
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
        <h4>Users FAVORITES</h4>
        <div id="cards">
          {!userFavorites && <p>Loading...</p>}
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
