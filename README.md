BẢN TIẾNG VIỆT

(CUỘN XUỐNG GIỮA FILE ĐỂ XEM BẢN TIẾNG ANH/SCROLL DOWN TO THE MIDDLE OF THE FILE TO SEE THE ENGLISH VERSION)


# PHÁT HIỆN MŨ BẢO HIỂM SỬ DỤNG YOLOv8

Đây là một dự án Computer Vision nhằm phát hiện mũ bảo hiểm của người đi xe máy và xe đạp bằng mô hình YOLOv8.

Dự án được xây dựng như một bài tập thực hành về Object Detection, tập trung vào các nội dung:

* Chuẩn bị dữ liệu
* Gán nhãn (Annotation)
* Huấn luyện YOLOv8
* Đánh giá mô hình
* Nhận diện trên ảnh thực tế

Mô hình cuối cùng có khả năng phát hiện mũ bảo hiểm trong các bức ảnh chứa người đi xe đạp hoặc xe máy trong nhiều điều kiện khác nhau.

# TỔNG QUAN DỰ ÁN

Dự án sử dụng:

* Python
* OpenCV
* PyTorch
* Ultralytics YOLOv8

Bộ dữ liệu:

* 1 lớp duy nhất: Helmet
* 1122 ảnh đã được gán nhãn
* Được tạo và tinh chỉnh bằng Roboflow

Cấu hình huấn luyện:

* Model: YOLOv8n
* Kích thước ảnh: 640x640
* Batch Size: 16
* Epochs: 30

# CẤU TRÚC THƯ MỤC

Project_2/
│
├── train.py
├── inference_images.py
├── inference_video.py
├── data.yaml
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
└── runs/

# CÀI ĐẶT

Clone repository bằng bash hoặc terminal:

git clone https://github.com/your_username/helmet-detection.git

cd helmet-detection

Cài đặt các thư viện cần thiết:

pip install -r requirements.txt

# DATASET

Dataset KHÔNG được đưa lên repository vì kích thước khá lớn.

Cấu trúc dataset mong muốn:

train/

valid/

test/

Mỗi thư mục bao gồm:

images/

labels/

Định dạng label theo chuẩn YOLO:

class_id center_x center_y width height

Ví dụ:

0 0.523 0.411 0.094 0.107

# HUẤN LUYỆN MÔ HÌNH

Để bắt đầu train model:

python train.py

Ví dụ nội dung train.py:

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
data="data.yaml",
epochs=30,
imgsz=640,
batch=16
)

# NHẬN DIỆN TRÊN ẢNH

Để nhận diện trên một ảnh:

python detect_image.py

Mô hình sẽ:

* Load trọng số đã train
* Phát hiện mũ bảo hiểm
* Vẽ bounding box
* Hiển thị kết quả

# NHẬN DIỆN TRÊN VIDEO

Để nhận diện trên video:

python detect_video.py

Chương trình sẽ thực hiện nhận diện từng frame theo thời gian thực.

# KẾT QUẢ HUẤN LUYỆN

Sau khoảng 30 epochs, mô hình đạt kết quả gần đúng:

* Precision ≈ 0.85
* Recall ≈ 0.65
* mAP@0.5 ≈ 0.75
* mAP@0.5:0.95 ≈ 0.41

Mô hình hoạt động khá tốt với:

* Người đi xe máy
* Người đi xe đạp
* Mũ bảo hiểm có kích thước trung bình

Mô hình hoạt động chưa thực sự tốt với:

* Mũ bảo hiểm quá nhỏ
* Người ở rất xa camera
* Ảnh bị nhòe hoặc rung mạnh

# HƯỚNG PHÁT TRIỂN TRONG TƯƠNG LAI

Một số hướng cải thiện có thể thực hiện:

* Mở rộng dataset
* Bổ sung nhiều điều kiện ánh sáng khác nhau
* Bài toán Helmet / No Helmet nhiều lớp
* Huấn luyện với YOLOv8s hoặc YOLOv8m
* Fine-tune từ các checkpoint tốt hơn
* Triển khai bằng Flask hoặc FastAPI
* Giám sát webcam theo thời gian thực




README.MD - ENGLISH VERSION


# HELMET DETECTION USING YOLOv8

A Computer Vision project for detecting motorcycle and bicycle helmets using YOLOv8.

The project was built as a practical object detection exercise focusing on:

- Dataset preparation
- Annotation and labeling
- YOLOv8 training
- Evaluation
- Real-world image inference

The final model is capable of detecting helmets from images containing riders, cyclists, and motorcyclists under different conditions.


# PROJECT OVERVIEW

This project uses:

- Python
- OpenCV
- PyTorch
- Ultralytics YOLOv8

Dataset:

- 1 Helmet class
- 1122 annotated images
- Automatically generated and refined using Roboflow

Training configuration:
- Model: YOLOv8n
- Image Size: 640x640
- Batch Size: 16
- Epochs: 30

# PROJECT STRUCTURE

Project_2/
│
├── train.py
├── inference_images.py
├── inference_video.py
├── data.yaml
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
└── runs/

# INSTALLATION

Clone the repository using bash or terminal:
"git clone https://github.com/your_username/helmet-detection.git

cd helmet-detection"

Install dependencies using bash or terminal:
pip install -r requirements.txt"

# DATASET

The dataset is NOT included in this repository because of its size.

The expected structure is:

train/
valid/
test/

Each folder contains:

images/
labels/

YOLO format labels:

class_id center_x center_y width height

Example output
0 0.523 0.411 0.094 0.107

# TRAINING

Start training:
On bash or terminal, type: 
"python train.py"

Example for train.py
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=30,
    imgsz=640,
    batch=16
)

# IMAGE INFERENCE

Run detection on an image using bash or terminal: 

"python detect_image.py"

The model will:

- Load the trained weights
- Detect helmets
- Draw bounding boxes
- Display the result


# VIDEO INFERENCE

Run detection on a video:

"python detect_video.py" run on bash or terminal

The model performs frame-by-frame detection in real time.

Training after 30 epochs produced approximately:
- Precision ≈ 0.85
- Recall ≈ 0.65
- mAP@0.5 ≈ 0.75
- mAP@0.5:0.95 ≈ 0.41

The model performs well on:
- Motorcycle riders
- Cyclists
- Medium-sized helmets
The model is less accurate on:
- Extremely small helmets
- Distant riders
- Heavy motion blur


# FUTURE IMPROVEMENTS
Possible improvements include:

- Larger dataset
- More diverse lighting conditions
- Helmet / No Helmet multi-class detection
- YOLOv8s or YOLOv8m training
- Fine-tuning from previous checkpoints
- Deployment using Flask or FastAPI
- Real-time webcam monitoring
