import numpy as np 
import matplotlib.pyplot as plt                                             
from PIL import Image

image_name = 'umerimg.jpeg'

try:
    img = Image.open(image_name).convert('L') 
    img.thumbnail((500, 500)) 
    img_array = np.array(img)
    
    # SVD calculations
    U, S, V = np.linalg.svd(img_array, full_matrices=False)

    # --- Naya Function: Storage calculate ---
    def get_info(k):
        m, n = img_array.shape
        # Original elements: m*n
        # Compressed elements: U (m*k) + S (k) + V (k*n)
        compressed_size = k * (m + n + 1)
        original_size = m * n
        ratio = (compressed_size / original_size) * 100
        return ratio

    # --- Expand: Multiple K-values comparison ---
    ks = [5, 25, 50, 150]
    plt.figure(figsize=(16, 9))

    for i, k in enumerate(ks):
        plt.subplot(2, 2, i+1)
        
        # Reconstruct image
        reconst = np.dot(U[:, :k], np.dot(np.diag(S[:k]), V[:k, :]))
        
        # Calculate space used
        space_used = get_info(k)
        
        plt.imshow(reconst, cmap='gray')
        plt.title(f"K = {k} | Space Used: {space_used:.2f}%")
        plt.axis('off')

    plt.suptitle("SVD Image Compression Analysis", fontsize=20)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    # ---  Singular Values Decay ---
    
    plt.figure(figsize=(8, 4))
    plt.plot(S)
    plt.title("Singular Values Magnitude (Importance of Data)")
    plt.xlabel("Index")
    plt.ylabel("Value")
    
    plt.show()

except Exception as e:
    print(f"Problem Occur: {e}")
