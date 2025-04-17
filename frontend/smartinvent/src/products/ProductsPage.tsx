import { useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import './ProductsPage.css'
import { logout } from '../../redux/authSlice'
import { useDispatch } from 'react-redux'
import { IoAccessibility } from "react-icons/io5"
import { IoAddCircleOutline } from "react-icons/io5"
import { IoLogOut } from "react-icons/io5"

interface Product {
  id: number
  name: string
  description: string
  price: number
}

const ProductsPage = () => {
  const [products, setProducts] = useState('')
  const [listProducts, setListProducts] = useState<Product[]>([])
  const total = useRef(0)
  const [error, setError] = useState('')
  const dispatch = useDispatch()


  const fetchProducts = async () => {
    try {
      const response = await axios.get('http://localhost:8000/products/', {
       withCredentials : true
    }) 
    if (typeof(response.data.message) == 'string'){
      setProducts(response.data.message)
    }else{
      setListProducts(response.data.product)
    }
      console.log(`Request: ${response.data}`)
      
    } catch (err) {
      setError('Failed to fetch products. Please try again later.')
      console.error(err)
    }
  }

  const fetchTotal = () => {
    axios.get('http://localhost:8000/products/total/',{
      withCredentials : true
    })
    .then(response => {
      total.current = response.data.count
    })
    .catch(err => {
      console.error(err)
    })
  }
  useEffect(() => {
    fetchProducts()
    fetchTotal()
  }, [])



  const logoutHandler = () => {
    axios.get('http://localhost:8000/users/logout/',{
      withCredentials: true,
    })
    .then(response => {
        dispatch(logout())
        console.log(response.data)
        navigate('/', {replace: true})
    })
    .catch((e) => {
      dispatch(logout())
      navigate('/', {replace: true})
      console.log(`Error: ${e}`)
      setError('The user has already been logged out')
    })
}



let navigate = useNavigate()

  return (
    <>
    <div className="products-container">
      <div className='logout-div'>
      <IoAccessibility onClick={() => { navigate('/update')}} />
      <IoLogOut onClick={logoutHandler} />
      <button onClick={() => navigate('/add-product')}>Create <IoAddCircleOutline /></button>
      </div>
      <div className='products-grid'>
        <h2>Total Products</h2>
        <p>{total.current}</p>
      </div>
      <h2>Products</h2>
      {error && <p className="error-message">{error}</p>}
      {products && <p>{products}</p>}
      {listProducts.length > 0 && (
      <div className="products-grid">
        {listProducts.map((product: Product) => (
          <div key={product.id} className="product-card" onClick={() => {navigate(`/update-product/${product.id}/`)}}>
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <p>Price: N{product.price}</p>
            <p>Quantity: {product.stock}</p>
          </div>
        ))}
      </div>
      )
    }
    </div>
    </>
  )
}

export default ProductsPage
