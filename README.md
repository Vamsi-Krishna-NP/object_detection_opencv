# Object Detection with Tkinter Interface

This project provides a desktop GUI for real-time object detection using OpenCV, Tkinter, and pyttsx3. The app displays your webcam feed, draws bounding boxes around detected objects, and announces their names using text-to-speech.

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