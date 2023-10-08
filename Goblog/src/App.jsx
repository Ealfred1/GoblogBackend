import { useState, useEffect } from 'react'
import Navbar from './Components/Navbar'
import Home from './Components/Home'
import BlogList from './Components/BlogList'

function App() {

  return (
    <>
      <div className="w-full h-screen bg-white">
        <Navbar />
        <Home />
      </div>
    </>
  )
}

export default App
