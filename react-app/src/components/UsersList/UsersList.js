import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";

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
      <div key={user.id}>
        <NavLink
          id="author-link"
          to={`/users/${user.id}`}
          style={({ textDecoration: "none" }, { color: "black" })}
        >
          <div>
            <img src={user.profileImg}></img>
          </div>
        </NavLink>
      </div>
    );
  });

  return (
    <>
      <h1>Authors: </h1>
      <ul>{userComponents}</ul>
    </>
  );
}

export default UsersList;