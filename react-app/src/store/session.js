import {authenticate} from '../services/auth'

const SET_USER = 'session/setUser';
const REMOVE_USER = 'session/removeUser';

export const setUser = (user) => ({
  type: SET_USER,
  payload: user
});

export const removeUser = () => ({
  type: REMOVE_USER
});

export const restoreUser = () => async (dispatch) => {
    let res = await authenticate();
    let data = res
    if(data.errors) data = {id: null}
    dispatch(setUser(data));
    return res;
  };

const initialState = { user: {id:null} };

function reducer(state = initialState, action) {
  let newState;
  console.log('action', action)
  switch (action.type) {
    case SET_USER:
      newState = Object.assign({}, state, { user: action.payload });
      return newState;
    case REMOVE_USER:
      newState = Object.assign({}, state, { user: {id:null} });
      return newState;
    default:
      return state;
  }
}

export default reducer;