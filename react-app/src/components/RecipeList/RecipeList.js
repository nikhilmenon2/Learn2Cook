import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";

function RecipeList() {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/api/recipes/");
      const responseData = await response.json();
      setRecipes(responseData.allrecipes);
    }
    fetchData();
  }, []);

  const recipeComponents = recipes.map((recipe) => {
    return (
      <div key={recipe.id}>
        <div>{recipe.title}</div>
        <NavLink to={`/recipes/${recipe.id}`}></NavLink>
      </div>
    );
  });

  return (
    <>
      <h1>Recipes: </h1>
      <div>{recipeComponents}</div>
    </>
  );
}

export default RecipeList;