import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { recipesDataDisplay } from "../../store/recipes";
import { useParams } from "react-router-dom";
import { NavLink } from "react-router-dom";
import Favorite from "../Favorite/Favorite";
import "./Recipe.css";
import WriteReview from "../WriteReview/WriteReview";
import ReactStars from "react-rating-stars-component";


function Recipe() {
  const dispatch = useDispatch();
  let recipe = useSelector((state) => state.recipes.recipe);
  let ingredients = useSelector((state) => state.recipes.ingredients);
  let instructions = useSelector((state) => state.recipes.instructions);
  let reviews = useSelector((state) => state.recipes.review);
  let users = useSelector((state) => state.recipes.users);
  let authors = useSelector((state) => state.recipes.author);
  const user = useSelector((state) => state.session.user);


  const { recipeId } = useParams();
  useEffect(() => {
    (() => {
      dispatch(recipesDataDisplay(recipeId));
    })();
  }, [dispatch, recipeId]);

  if (
    !recipe &&
    !ingredients &&
    !instructions &&
    !reviews &&
    !users &&
    !authors
  ) {
    return null;
  }



  const reviewcomp = reviews.map((review) => {
    return (
      <div className="reviewbox" key={review.id}>
        <NavLink to={`/recipes/${review.user.id}`}>
          <ReactStars
            count={5}
            size={24}
            value={review.overall}
            edit={false}
            activeColor="#ff0000"
          />
          <img className="picture-user" src={review.user.profileImg}></img>
        </NavLink>
        <div className="review-comment">"{review.review}"</div>
      </div>
    );
  });

  const instructionscomp = instructions.map((instructions) => {
    return (
      <div>
        <div className="instruction-step">Step {instructions.listOrder} </div>
        <br></br>
        <div>{instructions.specification} </div>
        <br></br>
      </div>
    );
  });


  return (
    <div id="parent-recipe-div">
      <div className="side-gold"></div>
      <div className="recipe">
        <div className="grid-wrap">
          <article>
            <h1 id="article-title">{recipe.title}</h1>
            <div id="author-div">
              <a id="author-link" href={`/users/${recipe.userId}`}>
                <h3 id="author">
                  By {authors.firstName} {authors.lastName}
                </h3>
              </a>
            </div>
            <div id="favorite-parent">
              <div id="under-author">
                <h3 className="time">
                  <span class="bigger">Yield</span> {recipe.servings} Servings
                </h3>
                <h3 className="time">
                  <span class="bigger">Time</span> {recipe.time} Minutes
                </h3>
              </div>
              <Favorite recipeId={recipeId} user={user} />
            </div>
            <div id="picture-container">
              <p id="article-description">{recipe.description}</p>
              <img id="recipe-picture" src={recipe.image}></img>
            </div>
            <div id="list-container">
              <div id="ingredient-container">
                <h3 className="heading-title">Ingredients</h3>
                {ingredients.map((ingredient) => (
                  <div id="ingredient-list">
                    {ingredient.amount} {ingredient.unit}{" "}
                    {ingredient.ingredientName}{" "}
                  </div>
                ))}
              </div>
              <div id="instruction-container">
                <h3 className="heading-title">Preparation</h3>
                <div id="instructions-list">{instructionscomp}</div>
              </div>
            </div>
            <div id="review-section">
              <div id="filler-div"></div>
              <div>
                <h3 className="heading-title">Reviews</h3>
                <WriteReview recipeId={recipeId} user={user} />
                <div id="review-parent-div">{reviewcomp}</div>
              </div>
            </div>
          </article>
        </div>
      </div>
      <div className="side-gold"></div>
    </div>
  );
}

export default Recipe;
