import os

def check(split):
    img_dir = f"images/{split}"
    lbl_dir = f"labels/{split}"

    imgs = {os.path.splitext(f)[0] for f in os.listdir(img_dir)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))}
    lbls = {os.path.splitext(f)[0] for f in os.listdir(lbl_dir)
            if f.lower().endswith(".txt")}

    print(f"\n--- {split} ---")
    print("Images:", len(imgs))
    print("Labels:", len(lbls))
    print("Images without labels:", len(imgs - lbls))
    print("Labels without images:", len(lbls - imgs))

for s in ["train", "val", "test"]:
    check(s)
