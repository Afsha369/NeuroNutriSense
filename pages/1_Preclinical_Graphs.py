import streamlit as st
from PIL import Image
import os
import base64

st.set_page_config(page_title="Preclinical Data", layout="wide")

# Custom CSS for hover zoom
st.markdown("""
    <style>
    .zoom:hover {
        transform: scale(1.05);
        transition: all 0.3s ease-in-out;
    }
    .thumb {
        width: 240px;
        margin: 10px;
        border-radius: 6px;
        box-shadow: 0 0 5px rgba(0,0,0,0.1);
    }
    .image-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: flex-start;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='font-size: 36px;'>🧪 Preclinical (Mouse Model) Data Visualizations</h1>
    <p style='font-size: 20px; color: #444;'>This section presents the experimental results from preclinical studies conducted by students of the Biotechnology department, RVCE. These studies track behavioral and neurochemical changes in mice under PD conditions and treatment interventions.</p>
""", unsafe_allow_html=True)

# Image directory
img_dir = "assets/preclinical_images"

# Section-wise image groups
image_sections = {
    "🔬 Setup & Protocol": [
        "Setup_Design.png",
        "Setup.png"
    ],
    "🧪 HPLC Results": [
        "HPLC_results1.png",
        "HPLC_results2.png"
    ],
    "🐀 Locomotor Activity": [
        "Locomotor_Activity1.png",
        "Locomotor_Activity2.png"
    ],
    "🌀 Rotarod Activity": [
        "Rotarod_Activity1.png",
        "Rotarod_Activity2.png"
    ]
}

# Create tabs for each section
tabs = st.tabs(list(image_sections.keys()))

for tab, (section, images) in zip(tabs, image_sections.items()):
    with tab:
        st.markdown(f"<h2 style='font-size: 26px; color:#4a4a4a;'>{section}</h2>", unsafe_allow_html=True)
        st.markdown('<div class="image-grid">', unsafe_allow_html=True)

        for file in images:
            img_path = os.path.join(img_dir, file)
            if os.path.exists(img_path):
                img = Image.open(img_path)
                thumbnail = img.resize((240, int(img.height * 240 / img.width)))

                with st.expander(f"🔍 View: {file}", expanded=False):
                    st.image(img, use_container_width=True)
            else:
                st.warning(f"⚠️ Image not found: {file}")

        st.markdown("</div>", unsafe_allow_html=True)


with st.expander("📌 Summary of Observations from Preclinical Studies", expanded=True):
    st.markdown("""
<div class="summary-text">
Behavioural assessments were carried out to investigate the effectiveness of combo drug and
methanol extract in MPTP induced PD mice models. Locomotor and Rotarod activity was
significantly increased on 14th, 21st, 28th day in MPTP mice models treated with combo-drug and
Methanol Extract.      

<br>

Based upon the behavioural performance of the MPTP models, we can conclude that combo-
drug containing l-dopa and ceftriaxone, which was designed and developed in our present
studies, has shown effect in PD models. It simultaneously enhances the dopamine synthesis and
also inhibits the aggregation of misfolded protein into lewy bodies in the brain. Effect of combo-
drug on Locomotor activity and Rotarod activity was found to be increasing in MPTP models.
Next to the Combo drug, Methanolic extract of Mucuna pruriens was also found to be more
effective than l-dopa in MPTP mice models.
</div>
""", unsafe_allow_html=True)
