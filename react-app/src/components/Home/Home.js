import React, { useEffect, useState } from "react";
import sample from './TrueClip.mp4';
import "./Home.css"
import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";
import { homeRecipesDisplay } from "../../store/recipes";
import { useDispatch, useSelector } from "react-redux";

function Home() {

  const [recipes, setRecipes] = useState([]);
  let recipearray = useSelector((state) => state.recipes.veg);
    const dispatch = useDispatch();

     useEffect(() => {
       (async () => {
         await dispatch(homeRecipesDisplay());
       })();
     }, [dispatch]);
      
      if (!recipearray) {
        return null;
      }


     const recipeComponents = recipearray.map((recipe) => {
        return (
          <a href={`/recipes/${recipe.id}`}>
            <div className="individual-box" key={recipe.id}>
              <div className="recipes-picture-box">
                <img className="recipes-picture" src={recipe.image}></img>
              </div>
              <div className="recipes-information-box">
                <h3>{recipe.title}</h3>
                <h5>Time: {recipe.time} Minutes</h5>
              </div>
            </div>
          </a>
        );
      });

 

    return (
      <div>
        <div id="videodiv">
          <video autoPlay loop muted playsInline>
            <source type="video/mp4" src={sample} />
          </video>
        </div>
        <div className="all-recipe-box">{recipeComponents}</div>
      </div>
    );
}

export default Home
 