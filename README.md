# Image Color Palette Extractor

This project is a fun and interactive Machine Learning mini-application that extracts the dominant colors from any uploaded image and generates a clean, visually appealing color palette. It uses clustering (K-Means) to identify the most representative colors and displays both HEX and RGB formats.

The goal of this project is to combine simple computer vision techniques with an intuitive UI to show how ML can be used to power creative, real-world applications.

---

## Core Features

- Extract dominant colors from any image (PNG/JPG/JPEG)
- Clean and aesthetic palette grid (Pinterest-style)
- HEX values for each color
- Auto-generated color names (HSL-based)
- Extract between 3 to 10 colors

---

## Designer & Developer Tools
- Copy all HEX values in one click
- Download palette as PNG
- Export palette as:
  - JSON
  - CSS variables
  - Tailwind config snippet

---

## Color Analysis Tools
- Color naming engine
- Color harmony suggestions:
  - Complementary
  - Analogous
  - Triadic

---

## Extra Visual Tools
- Smooth gradient previews between colors
- Palette history stored in session

---

## Optional Accessibility Tools
- Toggle: Show Accessibility Info (WCAG Contrast)
- View AA/AAA contrast ratings vs black & white
- Helps understand text readability

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – interactive web UI
- **Scikit-learn** – K-Means clustering
- **NumPy**
- **Pillow** – image handling
- **Custom modules for** 
  - Color naming
  - Harmony generation
  - WCAG contrast
  - PNG palette generation
  - Export formats

---

Image-Color-Palette-Extractor/
│── README.md
│── requirements.txt
│── data/
│── notebooks/
│   └── exploration.ipynb
│── src/
│   ├── app.py
│   └── palette/
│       ├── utils.py
│       ├── naming.py
│       ├── harmony.py
│       ├── wcag.py
│       ├── generate_png.py
│       └── export_formats.py


---

## ▶️ How to Run

1. Create a virtual environment
   python3 -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows

2. Install dependencies:

  pip install -r requirements.txt

3. Run the app:
   
  streamlit run src/app.py

4. Upload an image and view your generated color palette!
