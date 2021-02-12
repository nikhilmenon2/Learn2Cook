import React from 'react';
import './Footer.css';


function Footer() {
    return (
      <div className="footer-container">
        <div className="footer">
          <div id="logo-div">
          <a id="linkedinlogo" href="https://www.linkedin.com/in/nickmenon/" target="_blank">
            <i class="fab fa-linkedin fa-3x"></i>
          </a>
          <a id="githublogo" href="https://github.com/nikhilmenon2/Learn2Cook" target="_blank">
            <i class="fab fa-github fa-3x"></i>
          </a>
          <a id="angellogo" href="https://angel.co/u/nickmenon" target="_blank">
            <i class="fab fa-angellist fa-3x"></i>
          </a>
        </div>
        </div>
      </div>
    );
}

export default Footer
