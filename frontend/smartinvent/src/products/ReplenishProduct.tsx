import React, { useState } from 'react';
import { IoArrowBack } from "react-icons/io5";
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../users/SignUp.css';

const ReplenishProduct = () => {
  const [providerName, setProviderName] = useState('');
  const [defaultValue, setDefaultValue] = useState('');
  const [providerEmail, setProviderEmail] = useState('');
  const [address, setAddress] = useState('');
  const [providerNumber, setProviderNumber] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!providerName || !defaultValue || !providerEmail) {
      setMessage('Please fill in all fields.');
      return;
    }
    axios.post('http://localhost:8000/products/provider-form/',{
        providerName,
        defaultValue,
        providerEmail,
        address,
        providerNumber
    }, {
        withCredentials:true
    }).then(response => {
        console.log(`response: ${response.data.message}`);
        setMessage(response.data.message);
    })

   
  };

  return (
   <>
   <button onClick={() => {navigate('/products')}}> <IoArrowBack /> Back</button>
    <div className="signup-container">
      <h2>Product Restock Information</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name of Provider:</label>
          <input
            type="text"
            value={providerName}
            onChange={(e) => setProviderName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Default Restock Value:</label>
          <input
            type="number"
            value={defaultValue}
            onChange={(e) => setDefaultValue(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Provider Email:</label>
          <input
            type="text"
            value={providerEmail}
            onChange={(e) => setProviderEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Provider Address:</label>
          <input
            type="text"
            value={address}
            onChange={(e) => setAddress(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Provider Phone Number:</label>
          <input
            type="text"
            value={providerNumber}
            onChange={(e) => setProviderNumber(e.target.value)}
            required
          />
        </div>
        <button type="submit">Add Provider</button>
      </form>
      {message && <p>{message}</p>}
    </div>
    </>
  );
};

export default ReplenishProduct;
