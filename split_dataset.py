import os
import shutil
import random

# Configuration
DATA_DIR = 'data'
SPLITS = {
    'train': 0.8,
    'val': 0.1,
    'test': 0.1
}
RANDOM_SEED = 42

def prepare_dataset():
    # Target directories
    target_dirs = ['train', 'val', 'test']
    
    # Clean/Create target directories in root
    for d in target_dirs:
        if os.path.exists(d):
            print(f"Cleaning existing directory: {d}")
            shutil.rmtree(d)
        os.makedirs(d, exist_ok=True)

    if not os.path.exists(DATA_DIR):
        print(f"Error: {DATA_DIR} directory not found.")
        return

    # Categories are subfolders of data/
    categories = [d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))]
    print(f"Found categories: {categories}")

    for cat in categories:
        cat_path = os.path.join(DATA_DIR, cat)
        
        # Get all image files
        images = [f for f in os.listdir(cat_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
        
        random.seed(RANDOM_SEED)
        random.shuffle(images)
        
        num_images = len(images)
        train_end = int(num_images * SPLITS['train'])
        val_end = train_end + int(num_images * SPLITS['val'])
        
        train_imgs = images[:train_end]
        val_imgs = images[train_end:val_end]
        test_imgs = images[val_end:]
        
        print(f"\nProcessing category: {cat} ({num_images} images)")
        print(f"  - Train: {len(train_imgs)}")
        print(f"  - Val:   {len(val_imgs)}")
        print(f"  - Test:  {len(test_imgs)}")

        # Copy images to respective folders
        split_map = {
            'train': train_imgs,
            'val': val_imgs,
            'test': test_imgs
        }
        
        for split_name, img_list in split_map.items():
            dest_folder = os.path.join(split_name, cat)
            os.makedirs(dest_folder, exist_ok=True)
            
            for img_name in img_list:
                src = os.path.join(cat_path, img_name)
                dst = os.path.join(dest_folder, img_name)
                shutil.copy(src, dst)

    print(f"\nSuccessfully organized dataset into root folders:")
    print(f" - train/[category]/")
    print(f" - val/[category]/")
    print(f" - test/[category]/")

if __name__ == "__main__":
    prepare_dataset()
