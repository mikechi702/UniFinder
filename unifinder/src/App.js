import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch('/api/data')
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div className="App">
      <h1>React Frontend</h1>
      <p>{data.message}</p>
    </div>
  );
}

export default App;






