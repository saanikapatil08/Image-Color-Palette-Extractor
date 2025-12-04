# Image Color Palette Extractor 🎨

This project is a fun and interactive Machine Learning mini-application that extracts the dominant colors from any uploaded image and generates a clean, visually appealing color palette. It uses clustering (K-Means) to identify the most representative colors and displays both HEX and RGB formats.

The goal of this project is to combine simple computer vision techniques with an intuitive UI to show how ML can be used to power creative, real-world applications.

---

## 🚀 Features

- Upload any image (PNG/JPG/JPEG)
- Extract dominant colors using K-Means clustering
- Display color palette in HEX and RGB values
- Interactive Streamlit interface
- Simple, lightweight, and beginner-friendly

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – interactive web UI
- **Scikit-learn** – K-Means clustering
- **NumPy**
- **Pillow** – image handling

---

## 📁 Project Structure
image-color-palette-extractor/

│── README.md

│── requirements.txt

│── data/

│── src/

│ └── app.py

└── notebooks/

└── exploration.ipynb

---

## ▶️ How to Run

1. Install dependencies:
   
  pip install -r requirements.txt

3. Run the app:
   
  streamlit run src/app.py

4. Upload an image and view your generated color palette!
