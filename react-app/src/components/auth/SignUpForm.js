import React, { useState } from "react";
import { Redirect } from 'react-router-dom';
import { signUp } from '../../services/auth';
import { setLoginModal, setSignupModal } from '../../store/modal'
import { useDispatch } from 'react-redux'

const SignUpForm = ({authenticated, setAuthenticated}) => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [profileImg, setProfileImg] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const dispatch = useDispatch()

  const openLogin = (e) => {
    dispatch(setSignupModal(false))
    dispatch(setLoginModal(true))
  }
  const cancel = (e) => {
    dispatch(setSignupModal(false))
  }

  const onSignUp = async (e) => {
    e.preventDefault();

      const user = await signUp(username, email, password, repeatPassword, firstName, lastName, profileImg);
      if (!user.errors) {
        dispatch(setSignupModal(false))
        setAuthenticated(true);
      } else {
        setErrors(user.errors);
      }

  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updateProfileImg = (e) => {
    setProfileImg(e.target.value);
  };

  const updateFirstName = (e) => {
    setFirstName(e.target.value);
  };

  const updateLastName = (e) => {
    setLastName(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (

    <form onSubmit={onSignUp}>
      <h1 className='modal-title'>Sign Up</h1>
      <div>
        {errors.map((error) => (
          <div>{error}</div>
        ))}
      </div>
      <div className='modal-form-div'>
        <label>First Name</label>
        <input
          type="text"
          name="firstName"
          onChange={updateFirstName}
          value={firstName}
        ></input>
      </div>
      <div className='modal-form-div'>
        <label>Last Name</label>
        <input
          type="text"
          name="lastName"
          onChange={updateLastName}
          value={lastName}
        ></input>
      </div>
      <div className='modal-form-div'>
        <label>User Name</label>
        <input
          type="text"
          name="username"
          onChange={updateUsername}
          value={username}
        ></input>
      </div>
      <div className='modal-form-div'>
        <label>Email</label>
        <input
          type="text"
          name="email"
          onChange={updateEmail}
          value={email}
        ></input>
      </div>
      <div className='modal-form-div'>
        <label>Profile Image</label>
        <input
          type="text"
          name="profileImg"
          onChange={updateProfileImg}
          value={profileImg}
        ></input>
      </div>
      <div className='modal-form-div'>
        <label>Password</label>
        <input
          type="password"
          name="password"
          onChange={updatePassword}
          value={password}
        ></input>
      </div>
      <div className='modal-form-div'>
        <label>Repeat Password</label>
        <input
          type="password"
          name="repeat_password"
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
        ></input>
      </div>
      <div className='modal-button-box'>
          <div className='modal-link modal-button' onClick={onSignUp}>Sign Up</div>
          <div className='modal-link modal-button' onClick={openLogin}> Log In</div>
          <div className='modal-link modal-button' onClick={cancel}> Close</div>
        </div>
    </form>
  );
};

export default SignUpForm;
