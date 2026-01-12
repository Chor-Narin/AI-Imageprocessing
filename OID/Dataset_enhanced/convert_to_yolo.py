import os
import cv2

CLASS_NAME = "Cat"
CLASS_ID = 0

SPLITS = ["train", "val", "test"]

for split in SPLITS:
    img_dir = f"images/{split}"
    lbl_dir = f"labels/{split}"

    for label_file in os.listdir(lbl_dir):
        if not label_file.endswith(".txt"):
            continue

        img_name = label_file.replace(".txt", ".jpg")
        img_path = os.path.join(img_dir, img_name)

        if not os.path.exists(img_path):
            continue

        img = cv2.imread(img_path)
        h, w = img.shape[:2]

        new_lines = []

        with open(os.path.join(lbl_dir, label_file), "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 5:
                    continue

                cls, xmin, ymin, xmax, ymax = parts
                if cls != CLASS_NAME:
                    continue

                xmin = float(xmin)
                ymin = float(ymin)
                xmax = float(xmax)
                ymax = float(ymax)

                # convert to YOLO
                x_center = ((xmin + xmax) / 2) / w
                y_center = ((ymin + ymax) / 2) / h
                bw = (xmax - xmin) / w
                bh = (ymax - ymin) / h

                new_lines.append(
                    f"{CLASS_ID} {x_center:.6f} {y_center:.6f} {bw:.6f} {bh:.6f}"
                )

        with open(os.path.join(lbl_dir, label_file), "w") as f:
            f.write("\n".join(new_lines))
