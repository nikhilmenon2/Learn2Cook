import React from 'react';
import { useDispatch, useSelector } from 'react-redux';

const Modal = (props) => {
    const modals = useSelector(state => state.modal)
    const dispatch = useDispatch()
    if (!props.hidden) {
        // const cancel = (e) => {
        //     dispatch(props.cancel(false))
        // }

        return (
            <div className='modal-box-wrapper'>
                <div className='modal-box'>
                    {/* <div className='modal-text'></div> */}
                    {props.children}
                    {/* <div className='modal-button-box'> */}
                        {/* <div className='search-page-link modal-button'> Confirm</div> */}
                        {/* <div className='search-page-link modal-button' onClick={cancel}> Close</div>
                    </div> */}
                </div>
            </div>
            //  onClick={(e) => { setConfirmScreen(false) }}
            //   <div className="modal-box">
            //       {props.children}
            //   </div>
        );
    }
    return null
}

export default Modal;
