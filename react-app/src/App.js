import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import Home from "./components/Home/Home";
import { restoreUser } from "./store/session";
import { useDispatch } from "react-redux";
import Recipe from "./components/Recipe/Recipe";
import UsersList from "./components/UsersList/UsersList";
import UserProfile from "./components/UserProfile/UserProfile";
import RecipeList from "./components/RecipeList/RecipeList";
import CreateRecipe from "./components/CreateRecipe/CreateRecipe";


function App() {
  const [authenticated, setAuthenticated] = useState(false);
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();
  useEffect(() => {
    (async() => {
      const user = await dispatch(restoreUser())
      if(user) setAuthenticated(true);
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar setAuthenticated={setAuthenticated} />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm
            authenticated={authenticated}
            setAuthenticated={setAuthenticated}
          />
         </Route>
        <Route path="/" exact={true}>
          <Home />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm authenticated={authenticated} setAuthenticated={setAuthenticated} />
        </Route>
        <Route path="/recipes/create" exact={true} setAuthenticated={setAuthenticated}>
        <CreateRecipe/>
        </Route>
        <Route path="/recipes/" exact={true}> 
          <RecipeList/>
        </Route>
        <Route path="/recipes/:recipeId" exact={true}> 
          <Recipe/>
        </Route>
        <ProtectedRoute path="/users" exact={true} authenticated={authenticated}>
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true} authenticated={authenticated}>
         <UserProfile/>
        </ProtectedRoute>
        <ProtectedRoute path="/" exact={true} authenticated={authenticated}>
          <h1>My Home Page</h1>
        </ProtectedRoute>

      </Switch>
    </BrowserRouter>
  );
}

export default App;
