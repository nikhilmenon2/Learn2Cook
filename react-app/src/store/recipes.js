const RECIPES_DATA = '/recipes/recipedata';



const recipesdata = (recipe) => ({
    type: RECIPES_DATA,
    payload: recipe
})

export const recipesDataDisplay= (recipeId) => async (dispatch) => {
    let res = await fetch(`/api/recipes/${recipeId}`, {
        headers: {
            'Content-Type': 'application/json'
        }
    });
    res = await res.json();
    dispatch(recipesdata(res));
};

const initialState = { recipeInfo: null };

function reducer(state = initialState, action) {
    let newState;
    switch (action.type) {
        case RECIPES_DATA:
            newState = Object.assign({}, state, { ...action.payload });
            return newState;
        default:
            return state;
    }
}

export default reducer;
