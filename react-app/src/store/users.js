const CLEAR = '/users/clear'
const USER = '/users/user'

export const clear = () => ({
  type: CLEAR
});

const user = (user) => ({
  type: USER,
  payload: user
});

export const userData = (userId) => async (dispatch) => {
  let res = await fetch(`/api/users/no-auth/${userId}`, {
    headers: {
        'Content-Type': 'application/json'
    }
  });
  res = await res.json();
  dispatch(user(res));
}

const initialState = { 'users': [] };

function reducer(state = initialState, action) {
    let newState;
    switch (action.type) {
        case CLEAR:
            newState = { 'users': [] };
            return newState;
        case USER:
            newState = { 'users': [...state.users, action.payload ]};
            return newState;
        default:
          return state;
    }
}

export default reducer;