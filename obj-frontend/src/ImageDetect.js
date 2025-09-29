import React, { useState } from 'react';
import axios from 'axios';

function ImageDetect() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [results, setResults] = useState([]);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async () => {
  if (!selectedFile) return;
  window.liveSpeechEnabled = false;
  const formData = new FormData();
  formData.append('image', selectedFile);

  const response = await axios.post('http://localhost:5000/detect', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
  setResults(response.data.results);

  // Speak only the most confident label
  if (response.data.results.length > 0) {
    const best = response.data.results.reduce((a, b) => a.confidence > b.confidence ? a : b);
    const utterance = new window.SpeechSynthesisUtterance(best.label);
    window.speechSynthesis.speak(utterance);
  }
  setTimeout(() => {
    window.liveSpeechEnabled = true;
  }, 2000);
};

  return (
    <div className="card">
      <h2>Upload Image for Detection</h2>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button className="button" onClick={handleUpload}>Detect</button>
      <div>
        {results.map((item, idx) => (
          <div key={idx}>
            <strong>{item.label}</strong> - Confidence: {item.confidence.toFixed(2)}
          </div>
        ))}
      </div>
    </div>
  );
}

export default ImageDetect;