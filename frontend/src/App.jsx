// root of the appplication , also handles routing
import React from 'react'
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import Login from "./pages/Login" 
import Home from "./pages/Home"
import Register from "./pages/Register"
import NotFound from "./pages/NotFound" 
import ProtectedRoute from "./components/protectedRoute"  

function Logout(){
  localStorage.clear() 
  return <Navigate to="/Login"/>  
}

function RegisterAndLogout(){
  localStorage.clear() // make sure there are no old access tokens
   return <Register/>
}

function App() {

  return (
    <BrowserRouter>
       <Routes>
        <Route
          path="/"
          element= {
             <ProtectedRoute>
               <Home />
             </ProtectedRoute>
          }
        />
        <Route path="/login" element= {<Login />} />
        <Route path="/logout" element= {<Logout />} />  
        <Route path="/register" element= {<RegisterAndLogout />}/>
        <Route path="*" element= {<NotFound />}/> // 404 page for any other routes
         
       </Routes>
    </BrowserRouter>
  )
}

export default App
