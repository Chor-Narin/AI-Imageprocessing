import os
import cv2
import numpy as np

SPLITS = ["train", "val", "test"]
SRC_ROOT = r"Dataset\images"
DST_ROOT = r"Dataset_enhanced\images"

# Mild settings (safe): good for cats, low risk of hurting accuracy
CLAHE_CLIP = 2.0
ALPHA = 1.10  # contrast
BETA = 10     # brightness

def enhance(img):
    # CLAHE on L channel
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=CLAHE_CLIP, tileGridSize=(8, 8))
    l2 = clahe.apply(l)
    lab2 = cv2.merge((l2, a, b))
    out = cv2.cvtColor(lab2, cv2.COLOR_LAB2BGR)

    # brightness/contrast
    out = cv2.convertScaleAbs(out, alpha=ALPHA, beta=BETA)

    # sharpen (unsharp mask)
    blur = cv2.GaussianBlur(out, (0, 0), 1.2)
    out = cv2.addWeighted(out, 1.4, blur, -0.4, 0)

    return out

def process_split(split):
    src_dir = os.path.join(SRC_ROOT, split)
    dst_dir = os.path.join(DST_ROOT, split)
    os.makedirs(dst_dir, exist_ok=True)

    files = [f for f in os.listdir(src_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    total = len(files)

    for i, name in enumerate(files, 1):
        src_path = os.path.join(src_dir, name)
        dst_path = os.path.join(dst_dir, name)

        img = cv2.imread(src_path)
        if img is None:
            continue

        out = enhance(img)
        cv2.imwrite(dst_path, out)

        if i % 200 == 0 or i == total:
            print(f"{split}: {i}/{total}")

for s in SPLITS:
    process_split(s)

print("✅ Done. Enhanced images are in Dataset_enhanced/images/")
