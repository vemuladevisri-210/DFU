import streamlit as st

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------
st.set_page_config(
    page_title="Nearby Hospital Finder",
    page_icon="🏥",
    layout="wide"
)

# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background: linear-gradient(135deg, #E3F2FD, #BBDEFB, #E8F5FF);
}

.block-container{
    padding-top:2rem;
}

/* Header Card */
.header-card{
    background:linear-gradient(135deg,#1565C0,#42A5F5);
    color:white;
    padding:35px;
    border-radius:18px;
    text-align:center;
    box-shadow:0px 10px 25px rgba(0,0,0,.15);
}

.header-card h1{
    margin-bottom:10px;
}

.header-card p{
    font-size:18px;
}

/* Input Box */
div[data-baseweb="input"] input{
    border:2px solid #1565C0 !important;
    border-radius:12px !important;
    padding:14px !important;
    font-size:17px !important;
}

/* Buttons */
div.stButton > button{
    width:100%;
    height:50px;
    border-radius:12px;
    border:2px solid #1565C0;
    background:#1565C0;
    color:white;
    font-size:18px;
    font-weight:bold;
}

div.stButton > button:hover{
    background:white;
    color:#1565C0;
    border:2px solid #1565C0;
}

/* Result Card */
.result-card{
    background:white;
    border-radius:15px;
    padding:25px;
    text-align:center;
    border-left:6px solid #28a745;
    box-shadow:0px 5px 15px rgba(0,0,0,.1);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

left, center, right = st.columns([1,3,1])

with center:

    st.markdown("""
    <div class="header-card">

    <h1>🏥 Nearby Hospital Finder</h1>

    <p>
    Find nearby <b>Diabetic Foot Ulcer</b> treatment hospitals
    using your PIN Code.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown(
        "<h3 style='text-align:center;'>📍 Enter Your 6-Digit PIN Code</h3>",
        unsafe_allow_html=True
    )

    pin = st.text_input(
        "",
        placeholder="Example: 520001",
        max_chars=6,
        label_visibility="collapsed"
    )

    st.write("")

    if st.button("🔍 Search Nearby Hospitals", use_container_width=True):

        if len(pin) != 6 or not pin.isdigit():

            st.error("Please enter a valid 6-digit PIN Code.")

        else:

            google_map = f"https://www.google.com/maps/search/?api=1&query=diabetic+foot+ulcer+hospital+near+{pin}"

            st.markdown(f"""
            <div class="result-card">

            <h2>✅ Hospitals Found</h2>

            <p>
            Click the button below to open nearby hospitals in Google Maps.
            </p>

            </div>
            """, unsafe_allow_html=True)

            st.link_button(
                "📍 Open Google Maps",
                google_map,
                use_container_width=True
            )

    st.write("")
    st.write("")

    st.button(
        "⬅ Back to Dashboard",
        use_container_width=True,
        on_click=lambda: st.switch_page("app.py")
    )

    st.markdown("""
    <div class="footer">

    🏥 Diabetic Foot Ulcer Detection & Monitoring System

    </div>
    """, unsafe_allow_html=True)