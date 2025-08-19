import streamlit as st
from PIL import Image
from streamlit_extras.colored_header import colored_header

st.set_page_config(page_title="Comparative View", layout="wide")

colored_header(
    label="🔁 Comparative Analysis: Bridging Mouse and Human Studies",
    description="", 
    color_name="orange-70"
)

# Custom styled description below the header
st.markdown(
    "<div style='font-size:18px; font-weight:400; margin-top:-10px; margin-bottom:25px;'>"
    "This section connects key observations between preclinical mouse models and clinical patient datasets in Parkinson’s Disease."
    "</div>",
    unsafe_allow_html=True
)

# Load image function
def load_image(path):
    return Image.open(path)

# 1. Locomotor Activity Comparison
colored_header("1️⃣ Locomotor Activity: Clinical vs Preclinical", description="", color_name="violet-60")
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧬 Clinical: UPDRS Score by Exercise Level")
    st.image(load_image("assets/clinical_eda_graphs/updrs_by_exercise.png"), use_container_width=True)
    st.markdown("<h4 style='font-size:20px;'>🧠 Inference</h4>", unsafe_allow_html=True)
    with st.expander("Click to view details"):
        st.markdown("""
        <div style='font-size:16px; padding:12px; background-color:#f0f2f6; border-radius:8px; line-height:1.6;'>
        Patients with higher exercise levels show lower UPDRS scores, indicating better motor function.
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.subheader("🧪 Preclinical: Locomotor Activity under Treatment")
    st.image(load_image("assets/preclinical_images/Locomotor_Activity2.png"), use_container_width=True)
    st.markdown("<h4 style='font-size:20px;'>🧠 Inference</h4>", unsafe_allow_html=True)
    with st.expander("Click to view details"):
        st.markdown("""
        <div style='font-size:16px; padding:12px; background-color:#f0f2f6; border-radius:8px; line-height:1.6;'>
        Combo drug and methanolic extract improved mouse locomotor activity over 28 days.
        </div>
        """, unsafe_allow_html=True)

st.info("📌 Consistency Observed: Both models show improved motor function with physical or pharmacological intervention.")

# 2. Rotarod Test Comparison
colored_header("2️⃣ Rotarod Performance: Human Impairment vs Mouse Recovery", description="", color_name="blue-60")
col3, col4 = st.columns(2)

with col3:
    st.subheader("🧬 Clinical: Disease Progression vs Years Since Diagnosis")
    st.image(load_image("assets/clinical_eda_graphs/disease_progression_vs_years.png"), use_container_width=True)
    st.markdown("<h4 style='font-size:20px;'>🧠 Inference</h4>", unsafe_allow_html=True)
    with st.expander("Click to view details"):
        st.markdown("""
        <div style='font-size:16px; padding:12px; background-color:#f0f2f6; border-radius:8px; line-height:1.6;'>
        Disease stage stabilizes over time, indicating variable progression rates.
        </div>
        """, unsafe_allow_html=True)

with col4:
    st.subheader("🧪 Preclinical: Rotarod Activity under Treatment")
    st.image(load_image("assets/preclinical_images/Rotarod_Activity1.png"), use_container_width=True)
    st.markdown("<h4 style='font-size:20px;'>🧠 Inference</h4>", unsafe_allow_html=True)
    with st.expander("Click to view details"):
        st.markdown("""
        <div style='font-size:16px; padding:12px; background-color:#f0f2f6; border-radius:8px; line-height:1.6;'>
        Latency to fall improves with combo drug and extract, indicating neuromuscular recovery.
        </div>
        """, unsafe_allow_html=True)

st.info("📌 Insight: Clinical data shows plateauing symptoms, while mouse data reveals measurable improvement with treatment.")

# 3. Medication Response Comparison
colored_header("3️⃣ Medication Patterns: Patients vs Mouse Treatments", description="", color_name="blue-60")
col5, col6 = st.columns(2)

with col5:
    st.subheader("🧬 Clinical: UPDRS by Medication Type")
    st.image(load_image("assets/clinical_eda_graphs/updrs_by_medication.png"), use_container_width=True)
    st.markdown("<h4 style='font-size:20px;'>🧠 Inference</h4>", unsafe_allow_html=True)
    with st.expander("Click to view details"):
        st.markdown("""
        <div style='font-size:16px; padding:12px; background-color:#f0f2f6; border-radius:8px; line-height:1.6;'>
        UPDRS distributions are similar across medications with subtle median shifts.
        </div>
        """, unsafe_allow_html=True)

with col6:
    st.subheader("🧪 Preclinical: Comparative Drug Efficacy")
    st.image(load_image("assets/preclinical_images/Locomotor_Activity1.png"), use_container_width=True)
    st.markdown("<h4 style='font-size:20px;'>🧠 Inference</h4>", unsafe_allow_html=True)
    with st.expander("Click to view details"):
        st.markdown("""
        <div style='font-size:16px; padding:12px; background-color:#f0f2f6; border-radius:8px; line-height:1.6;'>
        Combo drug and extract outperformed L-dopa alone in improving locomotor activity.
        </div>
        """, unsafe_allow_html=True)

st.success("✅ This comparative lens underscores the translational potential of preclinical insights into patient-centered care strategies.")
