import React, {useState} from 'react'

function App() {
  const [file, setFile] = useState(false)

  const insertFile = () => setFile(true)

  return (
    <div>
      <form method="post" action="/run" encType="multipart/form-data">
        <input
          type="file"
          name="file"
          onChange={insertFile}
        />
        <button type="submit" disabled={!file}>Submit</button>
      </form>
    </div>
  );
}

export default App;
