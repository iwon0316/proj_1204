import React, { useState } from 'react';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000/filter/";

function FilterImage() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
	  console.log('Sending request to backend...');
      const response = await axios.post(API_URL, formData);  // API_URL 사용
      console.log('Response from backend:', response);
      setMessage(response.data.message);
    } catch (error) {
	  console.error('Error during API call:', error);
      setMessage("Error: " + error.response?.data?.error || error.message);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Filter Image</button>
      <p>{message}</p>
    </div>
  );
}

export default FilterImage;
