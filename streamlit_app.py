from click import option
import streamlit as st
from PIL import Image

st.set_page_config(page_title="PD Comparative Dashboard", layout="wide")

# Main Title
st.markdown("<h1 style='font-size:38px;'>🧠 Parkinson's Disease: Preclinical vs Clinical Comparative Study</h1>", unsafe_allow_html=True)

# Enhanced Welcome Text with Larger Font
st.markdown("""
<div style='font-size:19px; line-height:1.7'>
Welcome to a comprehensive exploration of Parkinson’s Disease progression based on:<br><br>

🧪 <b>Preclinical Animal Model Trials</b><br>
👥 <b>Clinical Patient Dataset Analysis</b><br><br>

This dashboard helps visualize and compare the patterns observed in both experimental and clinical contexts.
<br><br>
Below is an introductory snapshot related to the project. Click to enlarge and watch the full video.
</div>
""", unsafe_allow_html=True)

# Show clickable thumbnail inside expander
video_path = "assets/intro_video.mp4"
#thumbnail_path = "assets/intro_video_thumbnail.png" 

with st.expander("▶️ Click to View Introductory Video", expanded=False):
    st.video("assets/intro_video.mp4")
    st.markdown("<div style='text-align:center; font-size:14px; color:gray;'>Playing: Parkinson’s Disease project introduction video</div>", unsafe_allow_html=True)

st.markdown("---")

# Navigation section
st.markdown("<h2 style='font-size:26px;'>📂 Select a Module to Explore</h2>", unsafe_allow_html=True)
st.markdown("<div style='font-size:18px;'>Choose a section to dive into:</div>", unsafe_allow_html=True)

# Preclinical
st.markdown("🧪 <span style='font-size:16px;'>Explore visual results from <b>mouse-based experiments</b>, including behavioral and neurochemical tests.</span>", unsafe_allow_html=True)
st.page_link("pages/1_Preclinical_Graphs.py", label="👉 📊 Preclinical Trial Graphs", icon="🔬")

# Clinical
st.markdown("💊 <span style='font-size:16px;'>Analyze <b>patient data, medication effect, and lifestyle factors</b> from real-world clinical datasets.</span>", unsafe_allow_html=True)
st.page_link("pages/2_Clinical_EDA.py", label="👉 📈 Clinical EDA Visualizations", icon="📊")

# Comparative
st.markdown("🧠 <span style='font-size:16px;'>View a <b>side-by-side comparison</b> of trends in preclinical and clinical recovery patterns.</span>", unsafe_allow_html=True)
st.page_link("pages/3_Comparative_View.py", label="👉 🔁 Comparative View", icon="🧠")
