import React from 'react'
import { setLoginModal, setSignupModal } from '../../store/modal'
import { useDispatch } from 'react-redux'
import sample from './TrueClip.mp4';
import "./Home.css"


function Home() {

    return (
        <div>
            <div id="videodiv">
            <video autoPlay loop muted playsInline>
              <source type="video/mp4" src={sample} />
            </video>
            </div>
        </div>
    )
}

export default Home
