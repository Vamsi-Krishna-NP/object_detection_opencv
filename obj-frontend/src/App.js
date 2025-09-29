import React from 'react';
import './App.css';
import VideoStream from './VideoStream';
import ImageDetect from './ImageDetect';
// Import your logo
import logo from './assets/sential_ai_logo.png'; // Adjust path if needed

function App() {
  return (
    <div className="app-container">
      <div className="logo-section">
        <img src={logo} alt="Sentinel AI Logo" className="logo-img" />
        <h1>Sentinel AI</h1>
      </div>
      <VideoStream />
      <hr />
      <ImageDetect />
    </div>
  );
}

export default App;