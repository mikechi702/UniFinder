import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() { // function that takes a user input, then sends that to the backend, where the chatbot will respond to frontend.
  const [data, setData] = useState({});
  const [userInput, setUserInput] = useState('');

  useEffect(() => {
    fetchData(); // Initial data fetch
  }, []);

  const fetchData = async () => {
    try { // initial flask api call
      const response = await axios.get('http://localhost:5000/hello');
      setData(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:5000/api/data', { name: userInput });

      if (response.status === 200) {
        setData(response.data);
        setUserInput('');
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      {/* <h1>Unifinder</h1>
      <p>{data.message}</p>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
        <label>
          Enter your input:
          <input
            type="text"
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
          />
        </label>
        </div>
        <div className="form-group">
        <button type="submit">Submit</button>
        </div>
      </form> */}
    </div>
  );
}

export default App;



