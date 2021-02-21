import React, {useState, useEffect} from 'react'

function App() {
  const [file, setFile] = useState("")

  const fileInserted = (event) => setFile(event.target.value);

  const handleSubmit = (event) => {
    event.preventDefault()
  }
  
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" value={file} onChange={fileInserted}/>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
