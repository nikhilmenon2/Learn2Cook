import React from "react";
import { useDispatch } from 'react-redux'
import { setIncompleteModal } from '../../store/modal'
const IncompleteForm = () => {

  const dispatch = useDispatch()

  const cancel = (e) => {
    dispatch(setIncompleteModal(false))
  }

  return (
    <form > 
      <h1 className='modal-title'>Incomplete Form</h1>
      <div className='modal-form-div'>
        Please kindly fill the entire form to proceed. Thank you.
      </div>
      <div className='modal-form-div'>
        <div className='modal-button-box'>
          <div className='modal-link modal-button' onClick={cancel}> Close</div>
        </div>
      </div>
    </form>
  );
};

export default IncompleteForm;