import streamlit as st
from PIL import Image
import os
from streamlit_extras.colored_header import colored_header

# Page config
st.set_page_config(page_title="Clinical EDA Graphs", layout="wide")

# Title
st.markdown("## 🧪 Clinical Exploratory Data Analysis (EDA)")

# Image directory
img_dir = "assets/clinical_eda_graphs"

# Define images with captions
images = {
    "disease_progression_vs_years.png": "Disease progression stabilizes around stages 2 and 3 regardless of diagnosis duration, showing inter-patient variability.",
    "updrs_by_exercise.png": "Patients with higher exercise levels generally exhibit lower UPDRS scores, supporting physical activity as beneficial.",
    "pairplot_medication_progression.png": "Pramipexole shows higher density in later disease stages, suggesting medication-specific progression trends.",
    "medication_distribution_by_stage.png": "Levodopa and Pramipexole are more common in later stages, indicating flexible medication strategies.",
    "updrs_by_medication.png": "All medications show similar UPDRS spreads, suggesting variability in response or patient selection.",
    "updrs_by_disease_stage.png": "Slight drop in UPDRS scores with increasing disease stage implies non-linear progression or symptom fluctuation.",
    "updrs_over_years.png": "Mean UPDRS scores vary across years since diagnosis, reflecting treatment impact and patient diversity.",
    "updrs_by_gender.png": "Males tend to have slightly higher UPDRS scores than females, indicating potential gender-based symptom differences.",
    "updrs_vs_age.png": "Older patients tend to show higher UPDRS scores, suggesting increasing symptom severity with age.",
    "tremor_vs_age.png": "Tremor severity slightly increases with age, more visibly in males.",
    "speech_difficulty_by_gender.png": "Males show marginally higher speech difficulty scores, possibly due to symptom manifestation differences."
}

# Group images into categories
categories = {
    "📈 Disease Progression & Medication Impact": [
        "disease_progression_vs_years.png",
        "pairplot_medication_progression.png",
        "medication_distribution_by_stage.png",
        "updrs_by_medication.png",
        "updrs_by_disease_stage.png",
        "updrs_over_years.png",
    ],
    "💪 Exercise & Lifestyle": [
        "updrs_by_exercise.png"
    ],
    "👥 Demographics": [
        "updrs_by_gender.png",
        "updrs_vs_age.png",
        "tremor_vs_age.png",
        "speech_difficulty_by_gender.png"
    ]
}

# Loop through categories and display
for category, imgs in categories.items():
    colored_header(label=category, description="", color_name="blue-60")

    for i in range(0, len(imgs), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(imgs):
                with cols[j]:
                    img_file = imgs[i + j]
                    img_path = os.path.join(img_dir, img_file)
                    if os.path.exists(img_path):
                        st.image(Image.open(img_path), use_container_width=True)
                        st.markdown("<h4 style='font-size:20px;'>🧠 Inference</h4>", unsafe_allow_html=True)
                        with st.expander("Click to view details"):
                            st.markdown(f"""
                                <div style='font-size:16px; padding:12px; background-color:#f0f2f6;
                                            border-radius:8px; line-height:1.6;'>
                                    {images[img_file]}
                                </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.warning(f"Image not found: {img_path}")
