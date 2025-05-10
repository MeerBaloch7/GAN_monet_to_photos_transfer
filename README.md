# Monet Style Transfer using CycleGAN 🎨➡📸

This project implements a **CycleGAN** to perform **artistic style transfer** from Monet-style paintings to natural landscape photographs. It was developed as part of a machine learning assignment at NUST, with a focus on leveraging unpaired image-to-image translation using deep generative models.

---

## 📌 Objective

The goal is to explore **Generative Adversarial Networks (GANs)** for **style transfer**, specifically translating real-world photos into the impressionist style of Claude Monet. Given the absence of paired datasets, CycleGAN is used due to its ability to handle **unpaired image translation** effectively.

---

## 🧠 Model Overview

### 🔁 Architecture: CycleGAN

- **Generators**: ResNet-based architecture for both directions (Photo → Monet and Monet → Photo).
- **Discriminators**: PatchGAN-based, operating on 70x70 image patches.
- **Losses**:
  - **Adversarial Loss** – for image realism.
  - **Cycle Consistency Loss** – to preserve content.
  - **Identity Loss** – to preserve color when translating between same domains.

---

## 🧰 Dataset & Preprocessing

### 📥 Download Dataset

Run the following script to automatically download and extract the Monet dataset:

```bash
python download_data.py;
```
- ~300 Monet paintings and ~7000 landscape photos were used.
- Preprocessing:
  - Resized all images to **256×256**.
  - Data augmentation: **random crop**, **jitter**, and **horizontal flip**.

---

## 🏋️ Training Details

- Trained for **40+ epochs** using the **Adam optimizer**.
- **Learning rate scheduling** and **checkpointing** were implemented.
- Visual outputs saved at intervals to monitor training progression.

---

## 📊 Results

### ✅ Visual Output

- Successfully transferred Monet’s style to photos while maintaining scene structure.
- Demonstrated visible improvement in style adherence with training progress.

### 📉 FID Score

- **FID (Fréchet Inception Distance)**: `194.91`  
  *(Lower FID indicates higher image quality and diversity)*

---

## 🔍 Observations

### ✔ Strengths

- Effective use of CycleGAN for unpaired data.
- Strong augmentation and training loop structure.
- Regular visual evaluation for progress tracking.

### ❗ Areas for Improvement

- Computationally intensive (could benefit from downscaled images for early tests).
- No hyperparameter tuning or ablation studies conducted.
- Additional metrics (like Inception Score) could improve evaluation.

---

## 🧾 Conclusion

This project demonstrates a practical and effective use of **CycleGAN** for **artistic style transfer**. It shows that deep learning models can convincingly translate real-world content into impressionist art, opening avenues for creative AI applications in digital art and design.

---

## 📁 Files

- `ML_03.ipynb` – Main notebook containing full implementation.
- `monet_dataset/` – Contains Monet-style training images.
- `photo_dataset/` – Contains landscape photo dataset.
- `outputs/` – Generated images from training and testing.
- `checkpoints/` – Saved model weights and progress.

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/MeerBaloch7/GAN_monet_to_photos_transfer.git
cd monet-style-transfer-cyclegan

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook ML_03.ipynb
