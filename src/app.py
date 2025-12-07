import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import streamlit as st

from palette.utils import rgb_to_hex
from palette.generate_png import create_palette_image
from palette.export_formats import export_as_json, export_as_css, export_as_tailwind
from palette.naming import name_for_color
from palette.harmony import complementary, analogous, triadic
from palette.wcag import contrast_ratio, wcag_rating  # still needed if toggle ON

# Core Palette Extraction

def extract_palette(image: Image.Image, n_colors: int = 5):
    img = image.convert("RGB")
    pixel_array = np.array(img)
    pixels = pixel_array.reshape(-1, 3)

    kmeans = KMeans(n_clusters=n_colors, random_state=42, n_init=10)
    kmeans.fit(pixels)

    centers = kmeans.cluster_centers_.astype(int).tolist()
    return [rgb_to_hex(tuple(c)) for c in centers]

# UI Helper Functions

def render_palette_grid(hex_colors, theme="dark"):
    text_color = "#ffffff" if theme == "dark" else "#111111"

    cols = st.columns(len(hex_colors), gap="large")
    for col, hex_code in zip(cols, hex_colors):
        with col:
            st.markdown(
                f"""
                <div style="
                    width: 140px;
                    height: 140px;
                    background-color: {hex_code};
                    border-radius: 18px;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
                    transition: transform 0.25s ease;
                "
                onmouseover="this.style.transform='scale(1.09)'"
                onmouseout="this.style.transform='scale(1)'"
                >
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
                <p style="
                    text-align:center;
                    font-size:18px;
                    margin-top:12px;
                    color:{text_color};
                ">
                    <strong>{hex_code}</strong>
                </p>
                """,
                unsafe_allow_html=True,
            )


def render_copy_all_section(hex_colors):
    all_hex = ", ".join(hex_colors)
    st.subheader("Copy All HEX Values")
    st.code(all_hex, language="text")


def render_download_section(hex_colors):
    st.subheader("Download the palette here")

    img_buf = create_palette_image(hex_colors)
    st.download_button(
        label="Download Palette as PNG",
        data=img_buf,
        file_name="palette.png",
        mime="image/png",
    )

    json_str = export_as_json(hex_colors)
    css_str = export_as_css(hex_colors)
    tw_str = export_as_tailwind(hex_colors)

    with st.expander("Export as JSON"):
        st.code(json_str, language="json")

    with st.expander("Export as CSS Variables"):
        st.code(css_str, language="css")

    with st.expander("Export as Tailwind Config Snippet"):
        st.code(tw_str, language="javascript")


def render_naming_section(hex_colors):
    st.subheader("🎭 Find Color Names")
    for c in hex_colors:
        name = name_for_color(c)
        st.write(f"{c} → **{name}**")


def render_wcag_section(hex_colors):
    st.subheader("WCAG Contrast (vs White & Black)")
    for c in hex_colors:
        r_white = contrast_ratio(c, "#ffffff")
        r_black = contrast_ratio(c, "#000000")
        st.markdown(
            f"- {c}: vs **White** → {r_white:.2f} ({wcag_rating(r_white)}), "
            f"vs **Black** → {r_black:.2f} ({wcag_rating(r_black)})"
        )


def render_harmony_section(hex_colors):
    if not hex_colors:
        return
    base = hex_colors[0]
    st.subheader("🎨 Color Harmony (From First Color)")
    comp = complementary(base)
    analogs = analogous(base)
    triads = triadic(base)

    st.markdown("**Base Color:**")
    render_palette_grid([base])

    st.markdown("**Complementary:**")
    render_palette_grid([base, comp])

    st.markdown("**Analogous:**")
    render_palette_grid([base] + analogs)

    st.markdown("**Triadic:**")
    render_palette_grid([base] + triads)


def render_gradients_section(hex_colors):
    st.subheader("Gradient Previews")
    if len(hex_colors) < 2:
        st.info("Add at least 2 colors to see gradients.")
        return
    for c1, c2 in zip(hex_colors[:-1], hex_colors[1:]):
        st.markdown(
            f"""
            <div style="
                margin-top:10px;
                width: 100%;
                height: 60px;
                border-radius: 12px;
                background: linear-gradient(90deg, {c1}, {c2});
            ">
            </div>
            <p style="font-size:13px; margin-top:4px;">
                {c1} → {c2}
            </p>
            """,
            unsafe_allow_html=True,
        )


def update_palette_history(hex_colors):
    if "palette_history" not in st.session_state:
        st.session_state["palette_history"] = []
    if hex_colors and hex_colors not in st.session_state["palette_history"]:
        st.session_state["palette_history"].append(hex_colors)


def render_palette_history():
    history = st.session_state.get("palette_history", [])
    if not history:
        return
    st.subheader("Palette History Of This Session")
    for idx, palette in enumerate(history, start=1):
        st.markdown(f"**Palette {idx}:**")
        render_palette_grid(palette)

# Streamlit App

st.set_page_config(page_title="Image Color Palette Extractor", page_icon="🎨", layout="wide")

st.title("🎨 Image Color Palette Extractor")
st.write("Upload an image and generate a Coolors-style color palette with extra tools for designers and developers.")

# Theme selector
theme = st.sidebar.selectbox("Theme", ["dark", "light"])

if theme == "dark":
    page_bg = "#111111"
    text_color = "#ffffff"
else:
    page_bg = "#f5f5f5"
    text_color = "#111111"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {page_bg};
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
num_colors = st.slider("Number of colors to extract", 3, 10, 5)

current_palette = []

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Extracting colors..."):
        current_palette = extract_palette(image, num_colors)

    st.subheader("🎨 Extracted Palette")
    render_palette_grid(current_palette, theme=theme)

    # Update history
    update_palette_history(current_palette)

    st.divider()
    render_copy_all_section(current_palette)
    st.divider()
    render_download_section(current_palette)
    st.divider()
    render_naming_section(current_palette)
    st.divider()

    # WCAG Toggle Here

    show_wcag = st.checkbox("Show Accessibility Info (WCAG Contrast)", value=False)
    if show_wcag:
        render_wcag_section(current_palette)

    st.divider()
    render_harmony_section(current_palette)
    st.divider()
    render_gradients_section(current_palette)
    st.divider()
    render_palette_history()

else:
    st.info("Upload an image to get started.")
