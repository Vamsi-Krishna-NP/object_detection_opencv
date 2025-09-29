import React, { useState } from 'react';
import axios from 'axios';

function ImageDetect() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [results, setResults] = useState([]);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const speakLabels = (labels) => {
  if (labels.length === 0) return;
  const utterance = new window.SpeechSynthesisUtterance(labels.join(', '));
  window.speechSynthesis.speak(utterance);
  };

  const handleUpload = async () => {
  if (!selectedFile) return;
  const formData = new FormData();
  formData.append('image', selectedFile);

  const response = await axios.post('http://localhost:5000/detect', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
  setResults(response.data.results);

  // Speak detected labels
  const detectedLabels = response.data.results.map(item => item.label);
  speakLabels(detectedLabels);
  };

  return (
    <div>
      <h2>Upload Image for Detection</h2>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button onClick={handleUpload}>Detect</button>
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