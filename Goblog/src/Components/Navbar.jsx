const Navbar = () => {
  return (
  <header className="w-full flex justify-between items-center shadow shadow-sm
  shadow-gray-300 bg-gray-100 sticky mb-4 z-10 h-14 px-6 py-3">
    <div className="logo">
      <h2 className="sm:text-3xl text-xl font-medium text-blue-500 tracking-wider">Goblog.</h2>
    </div>
    
    <nav className="space-x-8 sm:space-x-4 text-sm sm:text-lg text-gray-400">
      <a className="hover:opacity-90" href="/"> Home</a>
      <a className="hover:opacity-90" href="/about"> About</a>
      <a className="hover:opacity-90" href="/create">Create Blog</a>
    </nav>
  </header>
  )
}

export default Navbar