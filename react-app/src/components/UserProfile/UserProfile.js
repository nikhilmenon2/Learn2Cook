import React, { useState, useEffect } from "react";
import { useParams, NavLink } from "react-router-dom";
import { useSelector } from 'react-redux';
// import Favorites from "./Favorites"




function User() {
    const [user, setUser] = useState({});
    // Notice we use useParams here instead of getting the params
    // From props.
    const { userId } = useParams();

    useEffect(() => {
        if (!userId) {
            return
        }
        (async () => {
            const response = await fetch(`/api/users/${userId}`);
            const user = await response.json();
            setUser(user);
        })();
    }, [userId]);

    const userState = useSelector(state => state.session.user)

    const sessId = userState.id
    console.log(userId)

    console.log(sessId)

    let isUserProfile

    if (userId === sessId) {
        isUserProfile = "a thing"
    }

    if (!user) {
        return null;
    }

    return (
        <>
            <div id="user-profile-container">
                <div id="img-box">
                    <img alt="nope" src={user.profileImg} />
                </div>
                <div id="user-info-box">
                    <div id="user-info-text">
                        <h3>{`${user.firstName} ${user.lastName}`}</h3>
                        <h5>{`Username: ${user.username}`}</h5>
                    </div>
                </div>
            </div>
            <div>
                {/* <Favorites sessionUser={userState} params={userId} /> */}
            </div>

        </>
    );
}
export default User;