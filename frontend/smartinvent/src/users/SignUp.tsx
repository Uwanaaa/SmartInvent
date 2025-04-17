import React, { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './SignUp.css';

const SignUp = () => {
  const [username, setName] = useState('');
  const [email, setEmail] = useState('');
  const [role, setRole] = useState('User');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const passwordInput = useRef<HTMLInputElement>(null)
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Basic validation
    if (!username || !email || !password) {
      setMessage('Please fill in all fields.');
      return;
    }
    axios.post('http://localhost:8000/users/create/',{
        username,
        email,
        role,
        password
    }).then(response => {
        console.log(`response: ${response.data.message}`);
        setMessage(response.data.message);
        navigate('/login')
    }).catch((e) => {
      console.log(`error: ${e}`);
    })
  };

  const showPassword = () => {
    const input = passwordInput.current
 
    if(input){
     input.type = input.type === 'password' ? 'text' : 'password'
    }
   }

  return (
    <div className="signup-container">
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor='roles'>Role:</label>
          <select name="roles" id="roles" value={role} onChange={(e) => {setRole(e.target.value)}}>
          <option value="User" selected>User</option>
          <option value="Admin">Admin</option>
          </select>
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            ref={passwordInput}
            required
          />
          <button type='button' onClick={() => {showPassword()}}>Show</button>
        </div>
        <button type="submit">Sign Up</button>
      </form>
      <p><a href="/login">Already have an account ?</a></p>
      {message && <p>{message}</p>}
    </div>
  );
};

export default SignUp;
