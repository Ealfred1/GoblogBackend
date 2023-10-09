import { useState, useEffect } from 'react'
import BlogList from './BlogList'
import useFetch from './useFetch'

const Home = () => {
  const { data: blogs, isLoading, error, } = useFetch('/api/blogs')
  
  return (
    <div className="mt-12 px-4">
      <h2 className="text-2xl text-center text-gray-400">Welcome to <span
      className="text-blue-500">Goblog.</span></h2>
      
      <div className="max-w-3xl mx-auto space-y-4">
       { blogs && <BlogList blogs={blogs} title='List Of all blog posts by different user' /> }
      { isLoading && <h2 className="text-2xl text-center text-blue-500">Getting Blogs...</h2> }
      { error && <h2 className="text-2xl text-center text-blue-500">{error}</h2> }
      </div>
    </div>
  )
}

export default Home