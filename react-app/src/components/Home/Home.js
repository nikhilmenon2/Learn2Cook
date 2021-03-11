import React, { useEffect, useState } from "react";
import sample from "./TrueClip.mp4";
import "./Home.css";
import "react-multi-carousel/lib/styles.css";
import { homeRecipesDisplay } from "../../store/recipes";
import { useDispatch, useSelector } from "react-redux";
import Carousel from "react-elastic-carousel";
import Footer from "../Footer/index";

function Home() {
  let vegarray = useSelector((state) => state.recipes.veg);
  let gfarray = useSelector((state) => state.recipes.gf);
  let chickenarray = useSelector((state) => state.recipes.chicken);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(homeRecipesDisplay());
    })();
  }, [dispatch]);

  if (!vegarray && !gfarray && !chickenarray) {
    return null;
  }

  const chickenrecipes = chickenarray.map((recipe) => {
    return (
      <a className="link" href={`/recipes/${recipe.id}`}>
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

  const vegrecipes = vegarray.map((recipe) => {
    return (
      <a className="link" href={`/recipes/${recipe.id}`}>
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
      <a className="link" href={`/recipes/${recipe.id}`}>
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

  const breakPoints = [
    { width: 1, itemsToShow: 1 },
    { width: 550, itemsToShow: 2, itemsToScroll: 2, pagination: false },
    { width: 850, itemsToShow: 3 },
    { width: 1150, itemsToShow: 4, itemsToScroll: 2 },
    { width: 1450, itemsToShow: 5 },
    { width: 1750, itemsToShow: 6 },
  ];

  return (
    <div>
      <div id="videodiv">
        <video autoPlay loop muted playsInline>
          <source type="video/mp4" src={sample} />
        </video>
      </div>
      <div id="home-parent-div">
        <div id="hometitlediv">
          <div id="random-title-div">
            <h3>What To Cook This Week</h3>
          </div>
        </div>
        <div id="spacing-div">
          <h1>🥬 Check out some Vegeterian Options 🥬</h1>
          <div className="carousel-div">
            <Carousel
              itemsToShow={5}
              itemPadding={[10, 50]}
              focusOnSelect={true}
              breakPoints={breakPoints}
            >
              {vegrecipes}
            </Carousel>
          </div>
          <div className="carousel-div">
            <h1>🌾 Check out some Gluten Free Options 🌾 </h1>
            <Carousel
              itemPadding={[10, 50]}
              focusOnSelect={true}
              breakPoints={breakPoints}
              itemsToShow={5}
            >
              {gfrecipes}
            </Carousel>
          </div>
          <div className="carousel-div">
            <h1>🐔 Get Some Chicken Dishes Tonight 🐔</h1>
            <Carousel
              itemPadding={[10, 50]}
              focusOnSelect={true}
              breakPoints={breakPoints}
              itemsToShow={5}
            >
              {chickenrecipes}
            </Carousel>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Home;
