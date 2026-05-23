import React, { useState } from 'react';
import './App.css'; // Import the CSS file

function App() {
  const [isLogin, setIsLogin] = useState(true);

  return (
    <div className="form-container">
      <h1>{isLogin ? "Login" : "Register"}</h1>
      
      <form className="auth-form">
        {!isLogin && <input type="text" placeholder="Full Name" />}
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        {!isLogin && <input type="password" placeholder="Confirm Password" />}
        
        <button type="submit">{isLogin ? "Login" : "Register"}</button>
      </form>

      <p className="toggle-text" onClick={() => setIsLogin(!isLogin)}>
        {isLogin ? "Don't have an account? Register." : "Already have an account? Login."}
      </p>
    </div>
  );
}

export default App;