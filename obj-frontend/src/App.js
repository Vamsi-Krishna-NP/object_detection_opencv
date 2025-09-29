import React from 'react';
import './App.css';
import VideoStream from './VideoStream';
import ImageDetect from './ImageDetect';

function App() {
  return (
    <div className="app-container">
      <h1>Object Detection App</h1>
      <VideoStream />
      <hr />
      <ImageDetect />
    </div>
  );
}

export default App;