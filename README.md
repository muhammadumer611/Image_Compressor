# 🖼️ Image Compression using SVD (Numpy)

This project uses **Singular Value Decomposition (SVD)** to compress images. It demonstrates how we can reduce the size of an image by keeping only the most important mathematical information (Singular Values).

## 🚀 How it Works
1. Loads an image and converts it to a **Numpy Array**.
2. Applies **SVD** to break the image into three matrices: $U, \Sigma, V$.
3. Reconstructs the image using only the top **K** features.
4. Compares different compression levels (K=5 to K=100).

## 📊 Visual Results
Here is how the image looks at different compression levels:

![Output Analysis](output.png)

## 🛠️ Tools & Libraries
- **Python**: Core logic
- **Numpy**: Matrix math and SVD
- **Matplotlib**: Displaying results
- **Pillow (PIL)**: Image processing

## 📈 Key Learnings
- Learned how images are stored as matrices.
- Understood the power of **Linear Algebra** in data science.
- Practiced Git/GitHub workflow for project management.
