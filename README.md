# Object Detection with Tkinter Interface

This project provides a desktop GUI for real-time object detection using OpenCV, Tkinter, and pyttsx3. The app displays your webcam feed, draws bounding boxes around detected objects, and announces their names using text-to-speech.

## Clone the Repository

To get started, clone this repository using:

```
git clone https://github.com/Vamsi-Krishna-NP/object_detection_opencv.git
```

## Requirements

All required Python packages are listed in `requirements.txt`.

## Installation

1. **Clone or download this repository.**

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Download model files and labels:**
   - Place `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt` and `frozen_inference_graph.pb` in the `resources` folder.
   - Place `Labels.txt` in the project root folder.

   You can get the COCO labels file [here](https://github.com/amikelive/coco-labels/blob/master/coco-labels-paper.txt).

## Usage

1. **Run the application:**
   ```
   python app.py
   ```

2. **Instructions:**
   - Click **Start Detection** to begin object detection.
   - Click **Stop Detection** to pause.
   - Close the window to exit.

## Notes

- Make sure your webcam is connected.
- If you want to use a different camera, change `self.video_source` in `app.py`.
- For best results, use the official COCO model and label files.

---

# Sentinel AI Web App (React + FastAPI)

This project also provides a web interface for object detection using a React frontend and FastAPI backend.

## Clone the Repository

To get started, clone this repository using:

```
git clone https://github.com/Vamsi-Krishna-NP/object_detection_opencv.git
```

## Requirements

- Python 3.7+
- Node.js & npm
- All Python and Node dependencies listed in `requirements.txt` and `package.json`
- COCO model files (`ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`, `frozen_inference_graph.pb`)
- COCO labels file (`Labels.txt`)

## Installation & Execution

1. **Install Python dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Install Node dependencies**
   ```
   cd obj-frontend
   npm install
   ```

3. **Prepare model and labels**
   - Place `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt` and `frozen_inference_graph.pb` in the `resources` folder.
   - Place `Labels.txt` in the project root.

4. **Run both backend and frontend**

   You can use the provided batch script (`run_all.bat`) or run manually:

   **Batch script (recommended):**
   ```
   @echo off
   start cmd /k "cd /d . && uvicorn backend:app --reload --port 5000"
   start cmd /k "cd /d obj-frontend && npm start"
   ```
   - Place this script in your project root and double-click to start both servers.

   **Manual:**
   - In one terminal, run:
     ```
     uvicorn backend:app --reload --port 5000
     ```
   - In another terminal, run:
     ```
     cd obj-frontend
     npm start
     ```

5. **Access the Web App**
   - Open [http://localhost:3000](http://localhost:3000) in your browser.

## Features

- Live object detection from webcam (FastAPI backend, React frontend)
- Upload image for detection
- Detected object names are spoken using browser speech synthesis
- Modern, professional UI with Sentinel AI branding

---

For any issues or questions, please refer to the documentation or contact the project maintainer.