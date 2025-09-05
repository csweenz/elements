import { useState } from 'react'
import './App.css'

function App() {
  const [msg, setMsg] = useState('');

  const fetchHello = async () => {
    const res = await fetch('http://localhost:8000/api/hello/');
    const data = await res.json();
    setMsg(data.message);
  };

  return (
    <div>
      <button onClick={fetchHello}>Say Hello</button>
      <p>{msg}</p>
    </div>
  )
}

export default App
