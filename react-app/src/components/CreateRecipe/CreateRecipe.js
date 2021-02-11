import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";

function CreateRecipe() {
  const history = useHistory();
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [veg, setVeg] = useState(false);
  const [cheap, setCheap] = useState(false);
  const [glutenFree, setGlutenFree] = useState(false);
  const [servings, setServings] = useState("");
  const [price, setPrice] = useState(0);
  const [image, setImage] = useState("");
  const [errors, setErrors] = useState([]);

  const userId = useSelector((state) => state.session.user.id);

  useEffect(() => {
    const errors = [];
    if (!title.length) {
      errors.push("Must input a name for your recipe!");
    }
    if (!description.length) {
      errors.push("Must input a description for your recipe");
    }
    if (!servings.length) {
      errors.push("Must include servings!");
    }
    if (!price.length) {
      errors.push(
        "Please tell us approx how much this recipe would cost per serving"
      );
    }
    if (image.length) {
      errors.push("Must Include Picture URL");
    }
    setErrors(errors);
  }, [title, description, servings, price, image]);

  const onSubmit = async (e) => {
    e.preventDefault();

    const formInfo = {
      title,
      description,
      veg,
      cheap,
      glutenFree,
      servings,
      price,
      image,
      userId,
    };

    let newRecipe = await fetch("/api/recipes/create", {
      method: "POST",
      header: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formInfo),
    });
    newRecipe = await newRecipe.json();
    history.push(`/recipes/${newRecipe.id}`);

    setTitle("");
    setDescription("");
    setServings("");
    setPrice("");
    setImage("");
  };

  return (
    <div id="create-recipe-parent">
      <form id="new-recipe-form" onSubmit={onSubmit}>
        <h2>Add Your Recipe</h2>
        <ul id="errors">
          {errors.map((error) => (
            <li key={error}>{error}</li>
          ))}
        </ul>
        <div>
          <label>Recipe Name </label>
          <input
            type="text"
            name="name"
            placeholder="Name of Recipe"
            onChange={(e) => setTitle(e.target.value)}
            value={title}
          />
        </div>
         <div>
          <label>Recipe Description </label>
        <textarea
          type="text"
          name="description"
          placeholder="Write a quick recipe description"
          onChange={(e) => setDescription(e.target.value)}
          value={description}
        />
        </div>
         <div>
          <label>Number of Servings </label>
        <input
          type="number"
          name="servings"
          onChange={(e) => setServings(e.target.value)}
          value={servings}
        />
        </div>
         <div>
          <label>Approx. Price per Serving? </label>
        <input
          type="number"
          name="price"
          placeholder="How much servings does this make?"
          onChange={(e) => setPrice(e.target.value)}
          value={price}
        />
        </div>
        <div>
            <label> Add Your Image URL </label>
          <input
            type="text"
            name="image"
            placeholder="Picture Url"
            onChange={(e) => setImage(e.target.value)}
            value={image}
          />
        </div>
        <div>
          <input
            type="checkbox"
            checked={veg}
            type="checkbox"
            onClick={(e) => setVeg(!veg)}
          />
          <label> Vegeterian?</label>
        </div>
        <div>
          <input
            label="cheap"
            type="checkbox"
            checked={cheap}
            type="checkbox"
            onClick={(e) => setCheap(!cheap)}
          />
          <label> Cheap?</label>
        </div>
        <div>
          <input
            type="checkbox"
            checked={glutenFree}
            type="checkbox"
            onClick={(e) => setGlutenFree(!glutenFree)}
          />
          <label> Gluten-Free?</label>
        </div>
        <button type="submit">Create Recipe</button>
      </form>
    </div>
  );
}
export default CreateRecipe;
