import cv2
import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk
import threading

# Load model and labels

config_file = "resources/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = "resources/frozen_inference_graph.pb"

model = cv2.dnn_DetectionModel(frozen_model, config_file)
model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

with open("Labels.txt", "rt") as fpt:
    ClassNames = fpt.read().rstrip('\n').split('\n')

engine = pyttsx3.init()

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()
        self.btn_start = tk.Button(window, text="Start Detection", width=20, command=self.start_detection)
        self.btn_start.pack()
        self.btn_stop = tk.Button(window, text="Stop Detection", width=20, command=self.stop_detection)
        self.btn_stop.pack()
        self.running = False
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def start_detection(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.update, daemon=True).start()

    def stop_detection(self):
        self.running = False

    def update(self):
        while self.running:
            ret, frame = self.vid.read()
            if not ret:
                break
            ClassIds, confs, bbox = model.detect(frame, confThreshold=0.5)
            spoken_labels = set()
            if len(ClassIds) != 0:
                for classId, confidence, box in zip(ClassIds.flatten(), confs.flatten(), bbox):
                    cv2.rectangle(frame, box, color=(0, 255, 0), thickness=2)
                    if 0 <= classId - 1 < len(ClassNames):
                        label = ClassNames[classId - 1]
                    else:
                        label = str(classId)
                    cv2.putText(frame, label, (box[0] + 10, box[1] + 40), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), thickness=2)
                    if label not in spoken_labels:
                        engine.say(label)
                        spoken_labels.add(label)
                engine.runAndWait()
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            self.window.update_idletasks()
            self.window.update()
            self.canvas.imgtk = imgtk  # Prevent garbage collection

    def on_closing(self):
        self.running = False
        self.vid.release()
        self.window.destroy()

if __name__ == "__main__":
    App(tk.Tk(), "Object Detection with Tkinter")