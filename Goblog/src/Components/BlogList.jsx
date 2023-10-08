
const BlogList = ({blogs, title}) => {
  const formatDate = (rawDate) => {
  return new Date(rawDate).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });
};

  return (
    <>
    <p className="text-lg text-gray-400 my-4">{title}</p>
    { blogs.map((blog) => (
      <div className="w-full shadow shadow-sm shadow-gray-300 h-20 px-3 py-5" key={blog.id}>
        <h2 className="text-blue-500 text-xl">{blog.title}</h2>
        
        <p className="text-right text-xs">{formatDate(blog.date_created)}</p>
      </div>
    )) }
    </>
  )
}

export default BlogList