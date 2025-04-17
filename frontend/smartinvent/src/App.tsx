import './App.css'


import SignUp from './users/SignUp'
import Login from './users/Login'
import ProductsPage from './products/ProductsPage'
import AddProduct from './products/AddProducts'
import UpdateProduct from './products/UpdateProducts'
import ReplenishProduct from './products/ReplenishProduct'
import UpdateReplenishProduct from './products/UpdateReplenishProduct'
import SetAlertValue from './products/SetAlertValue'
import Update from './users/Update'
import ProtectedRoute from './components/ProtectedRoute'
import { Routes,Route } from 'react-router-dom'

function App() {

  return (
    <Routes>
      <Route path="/signup" element={<SignUp />} />
      <Route path="/" element={<Login />} />
      <Route path="/update" element={<Update />} />

      <Route element={<ProtectedRoute />}>
        <Route path="/products" element={<ProductsPage />}>
          <Route path="add-product" element={<AddProduct />} />
          <Route path="update-product/:productId" element={<UpdateProduct />} />
          <Route path="provider-form" element={<ReplenishProduct />} />
          <Route path="update-provider-form/:providerId" element={<UpdateReplenishProduct />} />
        </Route>

        <Route path="/set-alert-value" element={<SetAlertValue />} />
      </Route>
    </Routes>
  );
}

export default App
