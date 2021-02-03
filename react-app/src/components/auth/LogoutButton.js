import React from "react";
import { logout } from "../../services/auth";
import { removeUser } from '../../store/session'
import { useDispatch } from 'react-redux'
import { useHistory } from "react-router-dom";



const LogoutButton = ({setAuthenticated}) => {
  const history = useHistory()
  const dispatch = useDispatch()
  const onLogout = async (e) => {
    history.push('/')
    await logout();
    dispatch(removeUser())
    setAuthenticated(false);
  };

  return <button id="logout" className="nav-link" onClick={onLogout}>Log-Out</button>;
};

export default LogoutButton;
