import os
from PIL import Image
import numpy as np

def make_images():
    # Create directories if they don't exist
    os.makedirs('sample_data/class_a', exist_ok=True)
    os.makedirs('sample_data/class_b', exist_ok=True)

    # Create 10 sample images for each class
    for i in range(10):
        # Create a blank white image for class_a
        img = Image.fromarray(np.ones((224, 224, 3), dtype=np.uint8) * 255)
        img.save(f'sample_data/class_a/img_{i}.png')

        # Create a blank black image for class_b
        img = Image.fromarray(np.zeros((224, 224, 3), dtype=np.uint8))
        img.save(f'sample_data/class_b/img_{i}.png')

    print("Sample images created in 'sample_data/'")
