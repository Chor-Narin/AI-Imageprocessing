# 🐱 Single-Class Object Detection: Cat Detection using YOLOv8

## Course
**AI & Image Processing**

## Project Title
**Single-Class Object Detection for Cat using Open Images Dataset and YOLOv8**

---

<h1>1. Project Overview</h1>
This project implements a **single-class object detection system** for detecting **Cats** using the **Open Images Dataset**.  
The project follows the complete object detection pipeline including:

- Dataset collection and preprocessing  
- Data cleansing and label validation  
- Application of **image processing techniques**  
- Model training using **YOLOv8**  
- Model evaluation and inference  
- Performance comparison **before and after data enhancement**

---

<h1>2. Dataset Description</h1>
- **Dataset Source**: Open Images Dataset (OID)
- **Object Class**: `Cat`
- **Total Images**: ~1,970 images

### Dataset Split
| Split | Images |
|------|--------|
| Train | 1,584 |
| Validation | 200 |
| Test | 186 |

### Final YOLO Dataset Structure
Dataset_enhanced/
├── images/
│ ├── train/
│ ├── val/
│ └── test/
├── labels/
│ ├── train/
│ ├── val/
│ └── test/


Each image has a corresponding YOLO label file with normalized bounding box coordinates.

---

<h1>3. Data Collection</h1>

The dataset was downloaded using the **OIDv4 / OIDv6 Toolkit** with the following commands:

```bash
python main.py downloader --classes Cat --type_csv train --limit 1500
python main.py downloader --classes Cat --type_csv validation --limit 200
python main.py downloader --classes Cat --type_csv test --limit 200
The dataset was then reorganized into a YOLO-compatible folder structure.
```

<h1>4. Data Preprocessing & Cleansing</h1>
4.1 Label Conversion

Original Open Images annotations were provided in pixel format:
```bash
Cat xmin ymin xmax ymax
```
These labels were converted into YOLO format:

```bash
class_id x_center y_center width height


- Cat → class ID 0
- Bounding boxes normalized to range [0, 1]
```

4.2 Dataset Validation

A validation script was used to ensure:
No missing image–label pairs
No corrupted files
Correct YOLO formatting


<h1>5. Image Processing Techniques (Data Enhancement)</h1>
<h2>Techniques Applied</h2>

<ul>
    <li>CLAHE (Contrast Limited Adaptive Histogram Equalization)</li>
    <li>Brightness and contrast adjustment</li>
    <li>Image sharpening (unsharp masking)</li>
</ul>

<h1>These enhancements improve:</h1>
Visibility of dark or low-contrast cats

Edge clarity

Overall image quality

<h1>6. Model Selection</h1>
<li>Model: YOLOv8n (Ultralytics)</li>
<li>Reason: Lightweight, fast, and suitable for CPU training while maintaining good accuracy</li>

<h1>7. Environment Setup</h1>
Requirements
```bash
pip install ultralytics opencv-python

Python 3.x

PyTorch (CPU)

OpenCV

<h1>8. Model Training</h1>
Training on Enhanced Dataset
yolo detect train \
  model=yolov8n.pt \
  data=data_enhanced.yaml \
  epochs=10 \
  imgsz=416 \
  batch=4 \
  mosaic=0 \
  plots=False \
  name=cat_enhanced


<h1>9. Model Evaluation</h1>
Evaluation was performed on the TEST dataset using:
yolo detect val \
  model=best.pt \
  data=data.yaml \
  split=test
<h1>11. Inference & Demo</h1>
Predict on Images
```bash
yolo detect predict \
  model=runs/detect/cat_enhanced/weights/best.pt \
  source=test_demo \
  conf=0.4 \
  save=True

