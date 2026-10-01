import streamlit as st

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Diabetic Foot Ulcer Detection System",
    page_icon="🦶",
    layout="wide"
)

# ---------------------------------
# Custom CSS
# ---------------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg, #E3F2FD, #BBDEFB, #E8F5FF);
}

/* Hide Streamlit Header */
#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

/* Main Title */
.main-title{
    text-align:center;
    font-size:58px;
    font-weight:800;
    color:#0B3D91;
    margin-top:20px;
    margin-bottom:8px;
}

/* Subtitle */
.sub-title{
    text-align:center;
    font-size:24px;
    color:#455A64;
    font-weight:500;
}

/* Quote */
.quote{
    text-align:center;
    font-size:20px;
    color:#1565C0;
    font-style:italic;
    margin-top:15px;
    margin-bottom:35px;
}

/* Welcome Card */
.welcome-card{
    background:#F4FAFF;
    padding:30px;
    border-radius:18px;
    box-shadow:0 8px 20px rgba(0,0,0,.12);
    text-align:center;
    margin-top:20px;
    margin-bottom:30px;
}

/* Feature Cards */
.feature-card{
    background:#EAF4FF;
    border:2px solid #B7DAFF;
    border-radius:18px;
    padding:30px 20px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
    transition:0.3s;
    height:260px;

    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
}
.feature-card:hover{
    transform:translateY(-5px);
}

.feature-title{
    font-size:22px;
    font-weight:bold;
    color:#0B3D91;
    margin-top:10px;
}

.feature-text{
    color:#555;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Header
# ---------------------------------

st.markdown("""
<div class="main-title">
🦶 Diabetic Foot Ulcer Detection System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
AI-Powered Early Detection using Hybrid Deep Learning
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="quote">
"Helping Detect Diabetic Foot Ulcers Early for Better Care and Better Outcomes."
</div>
""", unsafe_allow_html=True)

# ---------------------------------
# Welcome Card
# ---------------------------------

st.markdown("""
<div class="welcome-card">

<h2>👋 Welcome to the Application</h2>

<p style="font-size:18px; color:#555;">

This application assists in the early detection of
<b>Diabetic Foot Ulcers</b> by analyzing foot images using Artificial Intelligence.

It helps users identify ulcers, assess severity,
generate medical reports, and locate nearby hospitals
for timely medical care.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------------------------
# Features
# ---------------------------------
col1, col2, col3, col4 = st.columns(4)
with col1:

    st.markdown("""
    <style>
    .st-key-upload button{
        width:100%;
        height:280px;
        margin-top:-280px;
        opacity:0;
        border:none;
        cursor:pointer;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <div style="font-size:60px;">📷</div>
        <div class="feature-title">Upload Image</div>
        <div class="feature-text">
            Upload a clear foot image for AI analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("", key="upload", use_container_width=True):
        st.switch_page("pages/detect_ulcer.py")
with col2:

    st.markdown("""
    <style>
    .st-key-analysis button{
        width:100%;
        height:280px;
        margin-top:-280px;
        opacity:0;
        border:none;
        cursor:pointer;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <div style="font-size:60px;">📊</div>
        <div class="feature-title">AI Analysis</div>
        <div class="feature-text">
            Detect diabetic foot ulcers and estimate severity.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("", key="analysis", use_container_width=True):
        st.switch_page("pages/model_performance.py")
with col3:

    st.markdown("""
    <style>
    .st-key-report button{
        width:100%;
        height:280px;
        margin-top:-280px;
        opacity:0;
        border:none;
        cursor:pointer;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <div style="font-size:90px; line-height:1; margin-bottom:8px;">🤖</div>
        <div class="feature-title">AI Health Assistant</div>
        <div class="feature-text">
            Ask Questions About Diabetic Foot Ulcers
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("", key="report", use_container_width=True):
        st.switch_page("pages/ai_health_assistant.py")

with col4:

    st.markdown("""
    <style>
    .st-key-hospital button{
        width:100%;
        height:280px;
        margin-top:-280px;
        opacity:0;
        border:none;
        cursor:pointer;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <div style="font-size:60px;">🏥</div>
        <div class="feature-title">Find Hospital</div>
        <div class="feature-text">
            Locate nearby hospitals for diabetic foot care.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("", key="hospital", use_container_width=True):
        st.switch_page("pages/map.py")