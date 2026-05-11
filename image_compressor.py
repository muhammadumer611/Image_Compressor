import numpy as np 
import matplotlib.pyplot as plt                                             
from PIL import Image
import os

# 1. Image ka sahi rasta set karein
# Hum os library use kar rahe hain taake wo 'Image' folder ke andar dekh sakay
image_path = os.path.join('Image', 'umerimg.jpeg')

try:
    # 'cobvert' ko 'convert' kar diya hai
    img = Image.open(image_path).convert('L') 
    img_array = np.array(img)
    print("Original image shape:", img_array.shape)

    # 2. SVD Apply karein
    U, S, V = np.linalg.svd(img_array)

    def compress_image(K):
        # K ki value matrix se bari nahi honi chahiye
        K = min(K, S.shape[0])
        reconstructed_img = np.dot(U[:, :K], np.dot(np.diag(S[:K]), V[:K, :]))
        return reconstructed_img

    # 3. Visualization
    plt.figure(figsize=(12, 6))

    # Low Quality (k=5)
    plt.subplot(1, 2, 1)
    plt.imshow(compress_image(5), cmap='gray')
    plt.title("Too Much Compressed (k=5)")
    plt.axis('off')

    # Better Quality (k=50)
    plt.subplot(1, 2, 2)
    plt.imshow(compress_image(50), cmap='gray')
    plt.title("Better Quality (k=50)")
    plt.axis('off')

    plt.show()

except FileNotFoundError:
    print(f"Error: '{image_path}' nahi mili. Check karein ke image 'Image' folder ke andar hi hai?")
