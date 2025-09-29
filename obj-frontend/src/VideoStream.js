import React, { useEffect, useRef } from 'react';
import axios from 'axios';

function VideoStream() {
  const spokenLabelsRef = useRef([]);

  useEffect(() => {
    window.liveSpeechEnabled = true; // Add this line

    const interval = setInterval(async () => {
      if (!window.liveSpeechEnabled) return; // Skip speaking if disabled
      try {
        const response = await axios.get('http://localhost:5000/live_labels');
        const labels = response.data.labels || [];
        const newLabels = labels.filter(label => !spokenLabelsRef.current.includes(label));
        if (newLabels.length > 0) {
          const utterance = new window.SpeechSynthesisUtterance(newLabels.join(', '));
          window.speechSynthesis.speak(utterance);
          spokenLabelsRef.current = labels;
        }
      } catch (err) {}
    }, 1500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="video-center">
      <h2>Live Object Detection</h2>
      <img
        src="http://localhost:5000/video_feed"
        alt="Object Detection Stream"
        style={{ width: '640px', border: '2px solid #333' }}
      />
    </div>
  );
}

export default VideoStream;