import React, {useState} from 'react'

function App() {
  const [file, setFile] = useState(null);
  const fileInserted = (event) => setFile(event.target.value);
  const handleSubmit = async (event) => {
    event.preventDefault();
    if (file) {
      const data = new FormData();
      data.append("file", file);
      await fetch("/run", {
        method: "POST",
        body: data,
        headers: {
          "Content-type": "multipart/form-data"
        }
      }).then(res => res.json())
      .then(data => console.log(data.file))
      .catch(error => console.error(error))
    }
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          name="file"
          onChange={fileInserted}
        />
        <button type="submit" disabled={!file}>Submit</button>
      </form>
    </div>
  );
}

export default App;
