import React, { useState } from "react";
import Select from "react-select";
import { useDispatch, useSelector } from "react-redux";
import {
  setLoginModal,
  setIncompleteModal,
  setTextModal,
} from "../../../store/modal";

export default function WriteReview({ recipeId, user }) {
  const dispatch = useDispatch();

  const options = (category) => {
    return [
      { value: "1", label: `${category} 1` },
      { value: "2", label: `${category} 2` },
      { value: "3", label: `${category} 3` },
      { value: "4", label: `${category} 4` },
      { value: "5", label: `${category} 5` },
    ];
  };

  let reviewPresent;
  let reviewId;
  const recipes = useSelector((state) => state.recipes);
  if (
    recipes !== null &&
    typeof recipes !== "undefined" &&
    typeof recipes["1"] !== "undefined"
  ) {
    const reviews = recipes["1"]["reviews"];
    for (const review of reviews) {
      if (review["userId"] === user.id) {
        reviewPresent = review;
        reviewId = review["id"];
        break;
      }
    }
  }

  let overallPlaceholder;

  if (reviewPresent !== undefined) {
    console.log("here", reviewPresent);
    overallPlaceholder = reviewPresent["overall"];
  }

  const [overall, setOverall] = useState("");
  const [food, setFood] = useState("");
  const [service, setService] = useState("");
  const [ambience, setAmbience] = useState("");
  const [value, setValue] = useState("");
  const [review, setReview] = useState("Write your review here...");
  const setReviewWrapper = (e) => {
    setReview(e.target.value);
  };

  const postReview = (e) => {
    e.preventDefault();

    if (typeof user === "undefined" || user.id === null) {
      dispatch(setLoginModal(true));
    } else if (
      overall["value"] < 1 ||
      food["value"] < 1 ||
      service < 1 ||
      ambience < 1 ||
      value < 1 ||
      review.length < 1
    ) {
      // alert('Please fill out all sections of the review to complete your posting.')
      dispatch(setIncompleteModal(true));
    } else {
      const postReviewHere = async () => {
        await fetch(`/api/users/${user.id}/reviews/recipe/${recipeId}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            overall: overall,
            food: food,
            service: service,
            ambience: ambience,
            value: value,
            review: review,
          }),
        });
      };
      postReviewHere();

      dispatch(setTextModal(true));
      // alert('Thank you for your review!')
    }
  };

  const editReview = (e) => {
    e.preventDefault();
    // delete the old one
    if (
      overall["value"] < 1 ||
      food["value"] < 1 ||
      service < 1 ||
      ambience < 1 ||
      value < 1 ||
      review.length < 1
    ) {
      dispatch(setIncompleteModal(true));
      // alert('Please fill out all sections of the review to complete your posting.')
    } else {
      const editReviewHere = async () => {
        await fetch(`/api/users/${user.id}/reviews/${reviewId}`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
          },
          allow: "PATCH",
          body: JSON.stringify({
            overall: overall,
            food: food,
            service: service,
            ambience: ambience,
            value: value,
            review: review,
          }),
        });
      };
      editReviewHere();
      dispatch(setTextModal(true));
      // alert('Thank you for your review!');
    }
  };

  const deleteReview = async (e) => {
    e.preventDefault();

    await fetch(`/api/users/${user.id}/reviews/${reviewId}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });

    dispatch(setTextModal(true));

    // clear the stars and review box
    // reset the buttons
    // I want to re-run both.
  };

  return (
    <div id="writereview_container">
      {typeof reviewPresent === "undefined" ? (
        <h3 id="writereview_title">Write Your Review!</h3>
      ) : (
        <h3 id="writereview_title">Update Your Review!</h3>
      )}
      <div id="writereview_dropdown-container">
        <Select
          options={options("Overall")}
          className="writereview_dropdown-container-element"
          placeholder={`Overall ${overall}`}
          value={overall}
          onChange={setOverall}
        ></Select>
        <Select
          options={options("Food")}
          className="writereview_dropdown-container-element"
          placeholder={`Food ${food}`}
          value={food}
          onChange={setFood}
        ></Select>
        <Select
          options={options("Service")}
          className="writereview_dropdown-container-element"
          placeholder={`Service ${service}`}
          value={service}
          onChange={setService}
        ></Select>
        <Select
          options={options("Ambience")}
          className="writereview_dropdown-container-element"
          placeholder={`Ambience ${ambience}`}
          value={ambience}
          onChange={setAmbience}
        ></Select>
        <Select
          options={options("Value")}
          className="writereview_dropdown-container-element"
          placeholder={`Value ${value}`}
          value={value}
          onChange={setValue}
        ></Select>
      </div>
      <textarea
        id="writereview_textarea"
        placeholder={`${review}`}
        value={review}
        onChange={setReviewWrapper}
      ></textarea>
      {typeof reviewPresent === "undefined" ? (
        <button id="writereview_post" onClick={postReview}>
          Post Your Review!
        </button>
      ) : (
        <div id="writereview_post-and-delete-buttons">
          <button
            id="writereview_post"
            className="writereview_edit"
            onClick={editReview}
          >
            Edit Your Review!
          </button>
          <button
            id="writereview_post"
            className="writereview_delete"
            onClick={deleteReview}
          >
            Delete Your Review!
          </button>
        </div>
      )}
    </div>
  );
}
