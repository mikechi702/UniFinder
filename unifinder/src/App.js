import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    // Use Axios to make the API request
    axios.get('http://localhost:5000/api/data')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div className="App">
      <h1>React Frontend</h1>
      <p>{data.message}</p>
    </div>
  );
}

export default App;




