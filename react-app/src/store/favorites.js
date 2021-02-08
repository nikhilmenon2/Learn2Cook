const SET_USER_FAVORITES = 'userFavorites/setUserFavorites';
const ADD_FAVORITE = "add/addUserFavorites"
const DELETE_FAVORITE = "delete/deleteUserFavorites"

const setUserFavorites = (userFavorites) => ({
  type: SET_USER_FAVORITES,
  userFavorites
})

const addUserFavorites = (payload) => ({
  type: ADD_FAVORITE,
  payload
})

export const fetchUserFavorites = (userId) => {
  return async(dispatch) => {
    const response = await fetch(`/api/users/${userId}/favorites`)
    const data = await response.json()
    dispatch(
      setUserFavorites(data.favorites)
    )
  }
}

export const addFavorite = (recipeId, userId) => {
  return async (dispatch) => {
  
    let response = await fetch(`/api/users/${userId}/favorites/${recipeId}/add`, {
      
      method: "POST",
      header: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({recipeId, userId})
    })

    response = await response.json()

    dispatch(
      addUserFavorites(response))
    }
  }

const deleteUserFavorite = (payload) => ({
  type: DELETE_FAVORITE,
  payload
})

export const deleteFavorite = (recipeId, userId) => {
  return async (dispatch) => {
    let response = await fetch(`/api/users/${userId}/favorites/${recipeId}/delete`, {

      method: "DELETE",
      header: {
        "Content-Type": "application.json"
      },
      body: JSON.stringify({recipeId, userId})
    })
    response = await response.json()

    dispatch(deleteUserFavorite(response))
  }
}

const initialState = [];

function reducer(state = initialState, action) {
  let newState;
  switch (action.type) {
    case SET_USER_FAVORITES:
      newState = action.userFavorites
      return newState
    case ADD_FAVORITE:
      // newState = Object.assign({}, state, { ...action.payload });
      // newState.push(action.payload.recipe)
      // return newState;
       newState = state.push(action.payload.bar) //what is sapposed to be in place of User
      return newState;
    case DELETE_FAVORITE:
      newState = state.filter((fav) => {
        const ret = fav.id !== Number(action.payload.targetId)
        return ret
      })
      return newState
    default:
      return state;
  }
}

export default reducer;