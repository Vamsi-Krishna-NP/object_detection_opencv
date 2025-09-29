from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
import io

# Load model and labels
config_file = "resources/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = "resources/frozen_inference_graph.pb"
labels_file = "Labels.txt"

model = cv2.dnn_DetectionModel(frozen_model, config_file)
model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

with open(labels_file, "rt") as fpt:
    ClassNames = fpt.read().rstrip('\n').split('\n')

app = FastAPI()
camera = cv2.VideoCapture(0)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_labels = []

def update_latest_labels(frame):
    global latest_labels
    ClassIds, confs, bbox = model.detect(frame, confThreshold=0.5)
    labels = []
    if len(ClassIds) != 0:
        for classId in ClassIds.flatten():
            if 0 <= classId - 1 < len(ClassNames):
                labels.append(ClassNames[classId - 1])
    latest_labels = labels

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        update_latest_labels(frame)
        # Run detection
        ClassIds, confs, bbox = model.detect(frame, confThreshold=0.5)
        if len(ClassIds) != 0:
            for classId, confidence, box in zip(ClassIds.flatten(), confs.flatten(), bbox):
                cv2.rectangle(frame, box, color=(0, 255, 0), thickness=2)
                if 0 <= classId - 1 < len(ClassNames):
                    label = ClassNames[classId - 1]
                else:
                    label = str(classId)
                cv2.putText(frame, label, (box[0] + 10, box[1] + 40), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), thickness=2)
        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.get("/video_feed")
def video_feed():
    return StreamingResponse(gen_frames(), media_type='multipart/x-mixed-replace; boundary=frame')

@app.get("/live_labels")
def live_labels():
    return JSONResponse(content={'labels': latest_labels})

@app.post("/detect")
async def detect(image: UploadFile = File(...)):
    contents = await image.read()
    npimg = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    results = []
    ClassIds, confs, bbox = model.detect(frame, confThreshold=0.5)
    if len(ClassIds) != 0:
        for classId, confidence, box in zip(ClassIds.flatten(), confs.flatten(), bbox):
            if 0 <= classId - 1 < len(ClassNames):
                label = ClassNames[classId - 1]
            else:
                label = str(classId)
            results.append({
                'label': label,
                'confidence': float(confidence),
                'box': [int(x) for x in box]
            })
    return JSONResponse(content={'results': results})

# To run: uvicorn backend:app --reload --port 5000