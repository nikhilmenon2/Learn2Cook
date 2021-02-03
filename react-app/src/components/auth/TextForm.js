import React from "react";
import { useDispatch } from 'react-redux'
import { setTextModal } from '../../store/modal'
const TextForm = () => {

  const dispatch = useDispatch()

  const cancel = (e) => {
    dispatch(setTextModal(false))
  }

  return (
    <form > 
      <h1 className='modal-title'>Thank You</h1>
      <div className='modal-form-div'>
        Thank you. Your submission has been recorded.
      </div>
      <div className='modal-form-div'>
        <div className='modal-button-box'>
          <div className='modal-link modal-button' onClick={cancel}> Close</div>
        </div>
      </div>
    </form>
  );
};

export default TextForm;
