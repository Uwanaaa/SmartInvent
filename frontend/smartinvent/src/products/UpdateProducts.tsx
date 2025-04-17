import { useEffect, useRef, useState } from 'react';
import { IoArrowBack } from "react-icons/io5";
import { IoAddCircleOutline } from "react-icons/io5";
import { useParams,useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../users/SignUp.css';

const UpdateProduct = () => {
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [response, setResponse] = useState('')
  const [price, setPrice] = useState('')
  const [stock, setStock] = useState('')
  const [message, setMessage] = useState('')
  const [providerUpdateBtn, setProviderUpdateBtn] = useState(false)
  const [addProviderBtn, setAddProviderBtn] = useState(true)
  const providerValue = useRef(0)
  let { productId } = useParams()
  const navigate = useNavigate()


  const getProduct = () => {
    if (productId){
        axios.get(`http://localhost:8000/products/get-product/${productId}/`, {
            withCredentials:true
        }).then((response) => {
            console.log(`Data: ${response.data.provider_id}`);
            setName(response.data.name)
            setDescription(response.data.description)
            setPrice(response.data.price)
            setStock(response.data.stock)

            if (response.data.provider_id){
              providerValue.current = response.data.provider_id

              setProviderUpdateBtn(true)
              setAddProviderBtn(false)
            }
          }
        )
    }
    
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Basic validation
    if (!name || !description || !price || !stock) {
      setMessage('Please fill in all fields.');
      return;
    }
    axios.post(`http://localhost:8000/products/update-product/${productId}/`,{
        name,
        description,
        price,
        stock
    },{
      withCredentials: true
    }).then(response => {
        console.log(`response: ${response.data.message}`);
        setMessage(response.data.message);
    })
  };


  const deleteProduct = () => {
    axios.delete(`http://localhost:8000/products/delete-product/${productId}/`,{
      withCredentials: true
    })
    .then(() =>{
      // console.log(`Data: ${response.data}`);
      navigate('/products')
    }
    ).catch((e) => {
      console.log(`Error: ${e}`);
      setResponse('An error occurred while trying to delete the product')
    })
  }
  
  const UpdateProvider = () => {
    navigate(`update-provider-form/${providerValue.current}`)
  }

  useEffect(() => {
    getProduct()
  },[])
  return (
    <>
    <div>
    <button onClick={() => {navigate('/products')}}> <IoArrowBack /> Back</button>
    {providerUpdateBtn && <button onClick={UpdateProvider}> Update Provider <IoAddCircleOutline />  </button>}
    {addProviderBtn && <button onClick={() => {navigate('provider-form')}}> Add Provider <IoAddCircleOutline /> </button>}
    <button onClick={deleteProduct}>Delete</button>
    {response}
    </div>
    <div className="signup-container">
      <h2>Update Product</h2>
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
        <button type="submit">Update Product</button>
      </form>
      {message && <p>{message}</p>}
    </div>
    </>
  );
};

export default UpdateProduct;
