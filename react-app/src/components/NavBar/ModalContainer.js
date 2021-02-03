import React from 'react';
import { useDispatch, useSelector } from 'react-redux';

const Modal = (props) => {
    const modals = useSelector(state => state.modal)
    const dispatch = useDispatch()
    if (!props.hidden) {

        return (
            <div className='modal-box-wrapper'>
                <div className='modal-box'>
                    {props.children}
                
                </div>
            </div>
           
        );
    }
    return null
}

export default Modal;
