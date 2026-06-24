from ultralytics import YOLO
import os
import cv2
base_dir = os.path.dirname(__file__)

model_path = os.path.join(base_dir, "runs", "detect","train-4","weights","best.pt")
model = YOLO(model_path)

img_path = os.path.join(base_dir,"test_image2.jpg")

img = cv2.imread(img_path)

results = model(
    img_path,
    imgsz = 640
    )

annonated = results[0].plot()
annonated = cv2.resize(
    annonated,
    (640, 640)
)

cv2.imshow("helmet detection", annonated)

cv2.waitKey(0)
cv2.destroyAllWindows()