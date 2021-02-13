import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import "./UsersList.css";
import Footer from "../Footer/index";

function UsersList({ authenticated, setAuthenticated }) {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/api/users/");
      const responseData = await response.json();
      setUsers(responseData.users);
    }
    fetchData();
  }, []);

  const userComponents = users.map((user) => {
    return (
      <div className="authordiv" key={user.id}>
        <NavLink
          id="author-link"
          to={`/users/${user.id}`}
          style={({ textDecoration: "none" }, { color: "black" })}
        >
          <div>
            <img className="profile-img" src={user.profileImg}></img>
            <h3>{`${user.firstName} ${user.lastName}`}</h3>
          </div>
        </NavLink>
      </div>
    );
  });

  return (
    <>
      <div id="userparent">
        <h1>Chefs at Learn2Cook </h1>
        <div id="authorcontainer">{userComponents}</div>
      </div>
      <Footer />
    </>
  );
}

export default UsersList;
