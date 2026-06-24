from ultralytics import YOLO

import os
base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, "yolov8n.pt")
model = YOLO(model_path)
data_path = os.path.join(base_dir, "data.yaml")
model.train(
    data = data_path,
    epochs = 10,
    imgsz = 640,
    batch = 16
)