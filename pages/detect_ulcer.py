import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from report import generate_report

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="Detect Ulcer",
    page_icon="🦶",
    layout="wide"
)
# =====================================
# Custom Theme
# =====================================

st.markdown("""
<style>

/* Main Background */

.stApp{
    background: linear-gradient(135deg, #E3F2FD, #BBDEFB, #E8F5FF);
}


/* Center Title */
h1{
    text-align:center;
    color:#0B5394;
    font-size:42px;
    font-weight:700;
}

/* Center Paragraph */
p{
    text-align:center;
    font-size:18px;
}

/* Glass Card */
[data-testid="stVerticalBlock"]{
    background: rgba(255,255,255,0.75);
    border-radius:20px;
    padding:20px;
}

/* Text Input */
.stTextInput input{
    border-radius:12px;
    border:2px solid #2E86DE;
    padding:10px;
}

/* File Uploader */
[data-testid="stFileUploader"]{
      border-radius:12px;
    border:2px solid #2E86DE;
    background:#F8FBFF;
    padding:20px;
}

/* Buttons */
.stButton>button{
    background:#1976D2;
    color:white;
    border:none;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
    padding:10px 25px;
    transition:0.3s;
}

.stButton>button:hover{
    background:#0D47A1;
    transform:scale(1.05);
}

/* Download Button */
.stDownloadButton>button{
    background:#2E7D32;
    color:white;
    border-radius:10px;
    font-weight:bold;
}

/* Metric Cards */
[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0 4px 10px rgba(0,0,0,0.15);
}

/* Success */
.stSuccess{
    border-radius:10px;
}

/* Warning */
.stWarning{
    border-radius:10px;
}

/* Error */
.stError{
    border-radius:10px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#E3F2FD;
}

/* Remove top padding */
.block-container{
    padding-top:6rem;
    padding-bottom:2rem;
    max-width:1000px;
    margin:auto;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<h1>🦶 AI-Powered Diabetic Foot Ulcer Detection</h1>
<p style='text-align:center;font-size:20px;color:#444;'>
Upload a diabetic foot image for AI-based ulcer detection
</p>
""", unsafe_allow_html=True)

# =====================================
# Patient Name
# =====================================

st.markdown("<h3 style='text-align:center;'>👤 Patient Information</h3>", unsafe_allow_html=True)

patient_name = st.text_input(
    "",
    placeholder="Enter Patient Name"
)
st.markdown("<h3 style='text-align:center;'>📤 Upload Foot Image</h3>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "",
    type=["jpg","jpeg","png"]
)
# =====================================
# Load Model
# =====================================

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("dfu_2class_model.keras")

model = load_model()

classes = ["Healthy", "Ulcer"]

# =====================================
# Upload Image
# =====================================


# =====================================
# Prediction
# =====================================

if uploaded_file is not None:

    # Read image
    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Show uploaded image
    left, right = st.columns([1, 1])

    with left:
        st.image(
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
            caption="Uploaded Image",
            use_container_width=True
        )

    # -----------------------------
    # Image Preprocessing
    # -----------------------------
    img = cv2.resize(image, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)

    # -----------------------------
    # Prediction
    # -----------------------------
    prediction = model.predict(img, verbose=0)[0]

    class_index = np.argmax(prediction)

    confidence = float(np.max(prediction) * 100)

    label = classes[class_index]

    healthy_prob = float(prediction[0] * 100)
    ulcer_prob = float(prediction[1] * 100)

    with right:

        st.subheader("🔍 Prediction Result")

        if label == "Healthy":
            st.success(f"Prediction : {label}")
        else:
            st.error(f"Prediction : {label}")

        st.write(f"### Confidence : {confidence:.2f}%")

        st.progress(confidence / 100)

        st.markdown("### 📊 Probability")

        c1, c2 = st.columns(2)

        c1.metric("Healthy", f"{healthy_prob:.2f}%")
        c2.metric("Ulcer", f"{ulcer_prob:.2f}%")
        st.markdown("---")

    # =====================================
    # Healthy Case
    # =====================================

    if label == "Healthy":

        st.success("✅ No diabetic foot ulcer detected.")

        severity = "None"
        stage = "Healthy"
        wound_area = 0.0

        recommendations = [
            "Inspect your feet daily.",
            "Maintain normal blood sugar levels.",
            "Wear comfortable footwear.",
            "Keep feet clean and dry."
        ]

        st.subheader("🏥 Recommendations")

        for item in recommendations:
            st.success(f"✔ {item}")

    # =====================================
    # Ulcer Case
    # =====================================

    else:

        # Estimated severity based on confidence
        if confidence >= 95:
            severity = "Severe 🔴"
            stage = "Advanced Stage"

        elif confidence >= 80:
            severity = "Moderate 🟠"
            stage = "Progressive Stage"

        else:
            severity = "Mild 🟡"
            stage = "Early Stage"

        # Estimated wound area (demo calculation)
        wound_area = round(min(confidence / 5, 25), 1)

        st.subheader("🩺 Clinical Assessment")

        col1, col2, col3 = st.columns(3)

        col1.metric("Severity", severity)
        col2.metric("Healing Stage", stage)
        col3.metric("Estimated Wound Area", f"{wound_area}%")

        recommendations = [
            "Clean the wound daily.",
            "Maintain blood glucose levels.",
            "Avoid walking barefoot.",
            "Wear diabetic footwear.",
            "Consult a healthcare professional."
        ]

        st.subheader("🏥 Medical Recommendations")

        for item in recommendations:
            st.success(f"✔ {item}")

        if severity == "Severe 🔴":
            st.warning("⚠ Immediate medical consultation is recommended.")

    st.markdown("---")

    st.info(
        "⚠ This AI system is intended to assist healthcare professionals and should not replace clinical diagnosis."
    )
    # =====================================
# PDF Report Generation
# =====================================

st.markdown("---")

st.subheader("📄 Download Medical Report")

if st.button("📄 Generate PDF Report"):

    pdf_path = generate_report(
        patient_name=patient_name if patient_name else "Unknown",
        prediction=label,
        confidence=confidence,
        severity=severity,
        healing_stage=stage,
        wound_area=wound_area,
        recommendations=recommendations
    )

    st.success("✅ PDF Report Generated Successfully!")

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            label="⬇ Download Medical Report",
            data=pdf_file,
            file_name="DFU_Report.pdf",
            mime="application/pdf"
        )