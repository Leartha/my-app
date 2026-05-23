import React, { useState } from 'react';
import './LoginPage.css';

const LoginPage = () => {
  const [credentials, setCredentials] = useState({ username: '', password: '' });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCredentials(prev => ({ ...prev, [name]: value }));
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    console.log("Login submitted:", credentials);
    alert(`Welcome, ${credentials.username}!`);
  };

  return (
    <div className="login-wrapper">
      <form className="login-form" onSubmit={handleFormSubmit}>
        <h2>Sign In</h2>
        <div className="input-group">
          <label>Username</label>
          <input 
            name="username" 
            type="text" 
            placeholder="Enter your username" 
            onChange={handleInputChange} 
            required 
          />
        </div>
        <div className="input-group">
          <label>Password</label>
          <input 
            name="password" 
            type="password" 
            placeholder="Enter your password" 
            onChange={handleInputChange} 
            required 
          />
        </div>
        <button type="submit">Sign In</button>
      </form>
    </div>
  );
};

export default LoginPage;