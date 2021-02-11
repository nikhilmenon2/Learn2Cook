import React, { useState } from "react";
import ReactStars from "react-stars";
import { useDispatch, useSelector } from "react-redux";
import {
  setLoginModal,
  setIncompleteModal,
  setTextModal,
} from "../../store/modal";
import './WriteReview.css'


export default function WriteReview({ recipeId, user }) {
  const dispatch = useDispatch();

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
  const [review, setReview] = useState("");
  const setReviewWrapper = (e) => {
    setReview(e.target.value);
  };

  const postReview = (e) => {
    e.preventDefault();

    if (typeof user === "undefined" || user.id === null) {
      dispatch(setLoginModal(true));
    } else if (overall["value"] < 1 || review.length < 1) {
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
    if (overall["value"] < 1 || review.length < 1) {
      dispatch(setIncompleteModal(true));
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
            review: review,
          }),
        });
      };
      editReviewHere();
      dispatch(setTextModal(true));
      // alert('Thank you for your review!');
    }
  };
  console.log(overall)

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
        <ReactStars
          count={5}
          value={overall}
          onChange={setOverall}
          size={24}
          half={false}
          color2={'#ff0000'}
        />
  
      <textarea
        id="writereview_textarea"
        placeholder={"Please Comment Here"}
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
