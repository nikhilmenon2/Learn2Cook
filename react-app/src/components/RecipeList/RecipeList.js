import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import './RecipeList.css'
function RecipeList() {
  const [recipes, setRecipes] = useState([]);
  const [search, setSearch] = useState("");
  let recipearray = recipes
  
  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/api/recipes/");
      const responseData = await response.json();
      setRecipes(responseData.allrecipes);
    }
    fetchData();
  }, []);

    if (search.length > 0){
     recipearray = recipearray.filter((i) => {
       return i.title.toLowerCase().match(search)
     })
    }

  const recipeComponents = recipearray.map((recipe) => {
    return (
       <NavLink to={`/recipes/${recipe.id}`}>
      <div className="individual-box" key={recipe.id}>
        <div>{recipe.title}</div>
      </div>
      </NavLink>
    );
  });

  return (
    <>
    <div>
      <input type="text" placeholder="Search" onChange={event => {event.preventDefault(); setSearch(event.target.value)}}/>
    </div>
      <h1>Recipes: </h1>
      <div className="all-recipe-box">{recipeComponents}</div>
    </>
  );
}

export default RecipeList;