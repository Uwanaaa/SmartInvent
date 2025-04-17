import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useDispatch,useSelector } from 'react-redux'
import { login } from '../../redux/authSlice'
import axios from 'axios'
import './SignUp.css'

const Login = () => {
  const [username, setName] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')

  const navigate = useNavigate()
  const dispatch = useDispatch()

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    
  

    if (!username || !password) {
      setMessage('Please fill in all fields.')
      return
    }
    axios.post('http://localhost:8000/users/login/',{
        username,
        password
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(response => {
        console.log(`response: ${response.headers}`)
        dispatch(login('hi'))
        navigate('/products')
    }).catch(error => {
        dispatch(login('hi'))
        navigate('/products')
        console.error('Login error:', error.response ? error.response.data : error.message)
        if (error.message.detail){
          setMessage(error.message.detail)
        }
        setMessage('Login failed. Please check your credentials.')
    })
  }

  return (
    <div className="signup-container">
      <h2>Login</h2>
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
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
      <p><a href="/signup">No account ?</a></p>
      {message && <p>{message}</p>}
    </div>
  )
}

export default Login
