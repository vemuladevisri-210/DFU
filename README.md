# 🦶 Diabetic Foot Ulcer (DFU) Detection & Monitoring System

An AI-powered web application built with Streamlit and Deep Learning for early detection, severity assessment, and clinical monitoring of Diabetic Foot Ulcers.

---

## 🌟 Key Features

- **📷 AI-Powered Ulcer Detection**: Upload foot photographs to classify between *Healthy* and *Ulcer* using deep neural network models with confidence scores.
- **🩺 Severity & Wound Assessment**: Automatic estimation of ulcer severity stage and estimated wound area.
- **📄 Automated PDF Clinical Reports**: Download comprehensive medical evaluation reports in PDF format with recommendations.
- **🤖 AI Health Assistant**: Interactive Q&A for foot care guidelines, prevention tips, and diabetic ulcer information.
- **🏥 Nearby Hospital Locator**: Fast PIN code lookup to find nearby diabetic foot ulcer clinics and hospitals on Google Maps.
- **📊 Model Performance Metrics**: Comprehensive performance graphs, confusion matrix, precision, recall, and F1 scores.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/vemuladevisri-210/DFU.git
cd DFU
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```

---

## 📂 Project Architecture

```
DFU_Project/
│── app.py                    # Main dashboard and navigation entrypoint
│── requirements.txt          # Python dependencies for deployment
│── report.py                 # PDF clinical report generator
│── wound_area.py             # Wound contour and area analysis
│── gradcam.py                # Grad-CAM heatmap visualization
│── predict.py                # Inference script
│── train_model.py            # Model training script
│── dfu_2class_model.keras    # Pre-trained deep learning model
│── pages/
│   ├── detect_ulcer.py       # Detection & assessment page
│   ├── ai_health_assistant.py# Interactive health chatbot
│   ├── map.py                # Hospital locator by PIN code
│   ├── model_performance.py  # Model evaluation dashboard
│   └── about.py              # DFU education and information
```

---

## ☁️ Deployment

### Deploy to Streamlit Community Cloud:
1. Fork or push this repository to GitHub.
2. Visit [share.streamlit.io](https://share.streamlit.io/).
3. Connect your GitHub account and select repository `vemuladevisri-210/DFU`.
4. Set main file path as `app.py`.
5. Click **Deploy!**
