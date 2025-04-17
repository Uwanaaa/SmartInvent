import React, { FormEvent, useEffect, useState, useRef } from 'react'
import { IoArrowBack } from "react-icons/io5"
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import './SignUp.css'

const Update = () => {
  const [username, setName] = useState('')
  const [password, setPassword] = useState('')
  const [email, setEmail] = useState('')
  const [alert_value, setAlertValue] = useState('')
  const [message, setMessage] = useState('')
  const [data, setData] = useState({})
  const passwordInput = useRef<HTMLInputElement>(null)

  const navigate = useNavigate()

  const getUser = async() => {
    await axios.get(`http://localhost:8000/users/get-user/`,{
        withCredentials: true
    })
    .then((response) => {
        setName(response.data.username),
        setEmail(response.data.email),
        setAlertValue(response.data.alert_value)
    })
    .catch((e) => {
        console.log(`Error: ${e}`)
    })

    
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!username || !alert_value  ||!email) {
      setMessage('Please fill in all fields.')
      return
    }
    
    if (password !== ''){
       let data = {
            username,
            password,
            email,
            alert_value
        }

        setData(data)
    }else{
      let data = {
            username,
            email,
            alert_value
        }

        setData(data)
    }

    axios.post(`http://localhost:8000/users/update-user/`,data, {
      withCredentials: true,
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((response) => {
        setMessage(response.data.message)
    }).catch(error => {
        console.error('Update error:', error.response ? error.response.data : error.message)
        setMessage('Updating profile failed. Please try again.')
    })
  }

  const showPassword = () => {
   const input = passwordInput.current

   if(input){
    input.type = input.type === 'password' ? 'text' : 'password'
   }
  }

  useEffect(() => {
    getUser()
  }, [])

  return (
    <div className="signup-container">
        <button onClick={() => {navigate('/products')}}> <IoArrowBack /> Back</button>
      <h2>Profile</h2>
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
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            ref={passwordInput}
          >
            
            </input>
            <button type='button' onClick={() => {showPassword()}}>Show</button>
        </div>
        <div>
          <label>Alert Value:</label>
          <input
            type="text"
            value={alert_value}
            onChange={(e) => setAlertValue(e.target.value)}
            required
          />
        </div>
        <button type="submit">Save</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  )
}

export default Update
