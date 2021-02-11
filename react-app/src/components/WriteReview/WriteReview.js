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
  let reviewId;
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
    ;
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
        <button id="writereview_post" onClick={postReview}>
          Post Your Review!
        </button>
    </div>
  );
}
