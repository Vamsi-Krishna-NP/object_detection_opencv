// Spinner.js
import React from 'react';

export default function Spinner() {
  return (
    <div style={{
      display: 'flex', justifyContent: 'center', alignItems: 'center', height: '80px'
    }}>
      <div className="lds-ring"><div></div><div></div><div></div><div></div></div>
    </div>
  );
}