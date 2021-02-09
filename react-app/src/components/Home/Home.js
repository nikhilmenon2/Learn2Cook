import React, { useEffect, useState } from "react";
import sample from './TrueClip.mp4';
import "./Home.css"
import "react-multi-carousel/lib/styles.css";
import { homeRecipesDisplay } from "../../store/recipes";
import { useDispatch, useSelector } from "react-redux";
import Carousel from "react-elastic-carousel";
function Home() {

  const [recipes, setRecipes] = useState([]);
  let vegarray = useSelector((state) => state.recipes.veg);
  let gfarray = useSelector((state) => state.recipes.gf);
    const dispatch = useDispatch();

     useEffect(() => {
       (async () => {
         await dispatch(homeRecipesDisplay());
       })();
     }, [dispatch]);
      
      if (!vegarray && !gfarray) {
        return null;
      }
            
  const vegrecipes = vegarray.map((recipe) => {
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


  const gfrecipes = gfarray.map((recipe) => {
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
        <h1>Check out some Vegeterian Options</h1>
        <Carousel itemsToShow={5}>{vegrecipes}</Carousel>
        <h1>Check out some Gluten Free Options</h1>
        <Carousel itemsToShow={5}>{gfrecipes}</Carousel>
      </div>
    );
}

export default Home
 