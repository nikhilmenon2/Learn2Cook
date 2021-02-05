import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import "./RecipeList.css";
import { Input, InputGroup, InputLeftElement } from "@chakra-ui/react";
import { SearchIcon } from "@chakra-ui/icons";

function RecipeList() {
  const [recipes, setRecipes] = useState([]);
  const [search, setSearch] = useState("");
  let recipearray = recipes;

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/api/recipes/");
      const responseData = await response.json();
      setRecipes(responseData.allrecipes);
    }
    fetchData();
  }, []);

  if (search.length > 0) {
    recipearray = recipearray.filter((i) => {
      return i.title.toLowerCase().match(search.toLowerCase());
    });
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

  const HandleChange = (event) => {
    event.preventDefault();
    setSearch(event.target.value);
  };

  return (
    <>
      <div id="search-parent">
        <h1>Recipes </h1>
        <div id="search-container">
          <i class="fas fa-search"></i>
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
