import os
from PIL import Image
import imagehash

def remove_duplicates(image_dir):
    hashes = {}
    for img_file in os.listdir(image_dir):
        if img_file.endswith(('.jpg', '.png')):
            img_path = os.path.join(image_dir, img_file)
            try:
                hash_val = imagehash.average_hash(Image.open(img_path))
                if hash_val in hashes:
                    os.remove(img_path)
                    print(f"Removed duplicate: {img_file}")
                else:
                    hashes[hash_val] = img_path
            except Exception as e:
                os.remove(img_path)
                print(f"Removed corrupted {img_file}: {e}")

# Run for each split
remove_duplicates("OID/Dataset/train/Cat")
# Repeat for validation/test