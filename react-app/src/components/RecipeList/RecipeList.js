import React, { useEffect, useState } from "react";
import "./RecipeList.css";
import { Checkbox, Input } from "@chakra-ui/react";
// import CheckBox from "./CheckBox/CheckBox";

function RecipeList() {
  const [recipes, setRecipes] = useState([]);
  const [search, setSearch] = useState("");
  const [vegetarian, setVegetarian] = useState(false);
  const [glutenfree, setGlutenFree] = useState(false);
  let recipearray = recipes;

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/api/recipes/");
      const responseData = await response.json();
      setRecipes(responseData.allrecipes);
    }
    fetchData();
  }, []);

  if (vegetarian === true) {
    recipearray = recipearray.filter((i) => {
      return i.vegetarian == true;
    });
  }

  if (glutenfree === true) {
    recipearray = recipearray.filter((i) => {
      return i.glutenfree == true;
    });
  }

  if (search.length > 0) {
    recipearray = recipearray.filter((i) => {
      return i.title.toLowerCase().match(search.toLowerCase());
    });
  }

    const HandleChange = (event) => {
      event.preventDefault();
      setSearch(event.target.value);
    };

    const handleClick = () => setVegetarian(!vegetarian);
    const handleClick1 = () => setGlutenFree(!glutenfree);

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
    <>
      <div id="search-parent">
        <h1>Recipes</h1>
        <div id="search-container">
          <label>Vegeterian</label>
          <input
            name="vegeterian"
            type="checkbox"
            checked={vegetarian}
            onClick={handleClick}
          />
          <label> Gluten Free</label>
          <input
            name="glutenfree"
            type="checkbox"
            checked={glutenfree}
            onClick={handleClick1}
          />
          <label>  </label>
          <i class="fas fa-search fa-lg"></i>
          <Input
            id="search-bar"
            type="text"
            placeholder="Search"
            size="lg"
            color="gray.300"
            fontSize="1.2em"
            onChange={HandleChange}
          ></Input>
        </div>
      </div>

      <div className="all-recipe-box">{recipeComponents}</div>
    </>
  );
}

export default RecipeList;
