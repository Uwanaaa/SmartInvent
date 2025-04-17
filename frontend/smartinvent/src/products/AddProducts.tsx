import React, { useState } from 'react';
import { IoArrowBack } from "react-icons/io5";
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../users/SignUp.css';

const AddProduct = () => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [stock, setStock] = useState('');
  const [message, setMessage] = useState('');
  const [showProvider, setShowProvider] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Basic validation
    if (!name || !description || !price || !stock) {
      setMessage('Please fill in all fields.');
      return;
    }
    axios.post('http://localhost:8000/products/create-product/',{
        name,
        description,
        price,
        stock
    }, {
        withCredentials:true
    }).then(response => {
        if (response.status == 201){
          console.log(`response: ${response.data.message}`);
          setMessage(response.data.message);
          setShowProvider(true)
        }
        setMessage(response.data.message)
    })

   
  };

  return (
   <>
   <button onClick={() => {navigate('/products')}}> <IoArrowBack /> Back</button>
    <div className="signup-container">
      <h2>Add Product</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Description:</label>
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Price:</label>
          <input
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Stock:</label>
          <input
            type="number"
            value={stock}
            onChange={(e) => setStock(e.target.value)}
            required
          />
        </div>
        <button type="submit">Add new</button>
      </form>
      {message && <p>{message}</p>}
      {showProvider && <div>
        <p>Do you also want to add the supplier's information for automatic restock of goods when in low Quantity ?</p>
        <button onClick={() => {navigate('provider-form')}}>Yeah, sure</button>
        <button onClick={() => {navigate('/products')}}>No</button>
        </div>
        }
    </div>
    </>
  );
};

export default AddProduct;
