import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../users/SignUp.css';

const SetAlertValue = () => {
  const [alert_value, setAlertValue] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Basic validation
    if (!alert_value) {
      setMessage('Please fill in all fields.');
      return;
    }
    axios.post('http://localhost:8000/products/set-alert-value/',{
        alert_value
    }, {
        withCredentials:true
    }).then(response => {
        if (response.status == 201){
          console.log(`response: ${response.data.message}`);
          setMessage(response.data.message);
          navigate('/products')
        }
        setMessage(response.data.message)
    })

   
  };

  return (
   <>
    <div className="signup-container">
      <h2>Alert Value</h2>
      <p>This would be the minimum amount of items of a product that if reached would send an alert to your email and that of your supplier if provided.</p>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Alert Value:</label>
          <input
            type="text"
            value={alert_value}
            onChange={(e) => setAlertValue(e.target.value)}
            required
          />
        </div>
        <button type="submit">Add</button>
      </form>
      {message && <p>{message}</p>}
    </div>
    </>
  );
};

export default SetAlertValue;
