import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { login } from "../../services/auth";
import { useDispatch } from 'react-redux'
import { setUser } from '../../store/session'
import { setLoginModal, setSignupModal } from '../../store/modal'
const LoginForm = ({ authenticated, setAuthenticated }) => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const dispatch = useDispatch()
  const openSignup = (e) => {
    dispatch(setSignupModal(true))
    dispatch(setLoginModal(false))
  }
  const cancel = (e) => {
    dispatch(setLoginModal(false))
  }

  const onLogin = async (e) => {
    e.preventDefault();
    const user = await login(email, password);
    if (!user.errors) {
      setAuthenticated(true);
      dispatch(setLoginModal(false))
      dispatch(setUser(user))
    } else {
      setErrors(user.errors);
    }
  };

  const demoLogin = async (e) => {
    e.preventDefault();
    const user = await login('demo@aa.io', 'password');
    if (!user.errors) {
      setAuthenticated(true);
      dispatch(setLoginModal(false))
      dispatch(setUser(user))
    } else {
      setErrors(user.errors);
    }
  }

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (
    <form onSubmit={onLogin}>
      <h1 className='modal-title'>Log In</h1>
      <div>
        {errors.map((error) => (
          <div>{error}</div>
        ))}
      </div>
      <div className='modal-form-div'>
        <label htmlFor="email">Email</label>
        <input
          name="email"
          type="text"
          placeholder="Email"
          value={email}
          onChange={updateEmail}
        />
      </div>
      <div className='modal-form-div'>
        <label htmlFor="password">Password</label>
        <input
          name="password"
          type="password"
          placeholder="Password"
          value={password}
          onChange={updatePassword}
        />
        <div className='modal-button-box'>
          <div className='modal-link modal-button' onClick={onLogin}>Login</div>
          <div className='modal-link modal-button' onClick={openSignup}> Sign Up</div>
          <div className='modal-link modal-button' onClick={cancel}> Close</div>
        </div>
        <div className='modal-button-box'>
          <div className='modal-link modal-button' onClick={demoLogin}>Demo Login</div>
        </div>

      </div>
    </form>
  );
};

export default LoginForm;
