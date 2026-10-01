import streamlit as st

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="AI Health Assistant",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# Custom Theme
# =====================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#E3F2FD,#BBDEFB,#E8F5FF);
}

.block-container{
    max-width:900px;
    margin:auto;
    padding-top:3rem;
}

h1{
    text-align:center;
    color:#0B5394;
}

.stTextInput input{
    border-radius:12px;
    border:2px solid #1976D2;
    padding:12px;
}

.stButton>button{
    background:#1976D2;
    color:white;
    border:none;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
    width:100%;
}

.answer{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.15);
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# Title
# =====================================

st.title("🤖 AI Health Assistant")

st.markdown(
"""
Ask questions related to **Diabetic Foot Ulcers**, symptoms,
prevention, wound care, treatment, and diabetes management.
"""
)

# =====================================
# Questions
# =====================================

questions = {

"What is a diabetic foot ulcer?":
"A diabetic foot ulcer is an open sore or wound that commonly develops on the feet of people with diabetes due to poor blood circulation and nerve damage.",

"What are the symptoms of diabetic foot ulcer?":
"Common symptoms include redness, swelling, pain, drainage, foul odor, skin discoloration, and slow healing wounds.",

"How can I prevent diabetic foot ulcers?":
"Inspect your feet daily, maintain blood sugar levels, wear comfortable footwear, keep feet clean and dry, and avoid walking barefoot.",

"What should I do if I have an ulcer?":
"Clean the wound, avoid pressure on the affected foot, maintain blood sugar levels, and consult a healthcare professional immediately.",

"What foods help wound healing?":
"Protein-rich foods, leafy vegetables, fruits rich in Vitamin C, zinc-rich foods, and adequate water intake support wound healing.",

"When should I visit a doctor?":
"Seek immediate medical care if the ulcer becomes larger, shows pus, has a bad smell, increased redness, swelling, or fever.",

"Can diabetic foot ulcers heal?":
"Yes. With early diagnosis, proper wound care, blood sugar control, and medical treatment, many diabetic foot ulcers heal successfully.",

"How often should I check my feet?":
"People with diabetes should inspect their feet every day for cuts, blisters, redness, swelling, or other changes."

}

# =====================================
# Select Question
# =====================================

selected = st.selectbox(
    "Choose a Question",
    list(questions.keys())
)

if st.button("Get Answer"):

    st.markdown(
        f"""
<div class="answer">
<h3>💬 Answer</h3>
<p>{questions[selected]}</p>
</div>
""",
        unsafe_allow_html=True
    )

# =====================================
# Ask Your Own Question
# =====================================

st.markdown("---")

st.subheader("💬 Ask Your Own Question")

user_question = st.text_input("Type your question here")

if st.button("Ask AI"):

    q = user_question.lower()

    if "symptom" in q:
        ans = questions["What are the symptoms of diabetic foot ulcer?"]

    elif "prevent" in q:
        ans = questions["How can I prevent diabetic foot ulcers?"]

    elif "food" in q:
        ans = questions["What foods help wound healing?"]

    elif "doctor" in q or "hospital" in q:
        ans = questions["When should I visit a doctor?"]

    elif "heal" in q:
        ans = questions["Can diabetic foot ulcers heal?"]

    elif "ulcer" in q:
        ans = questions["What is a diabetic foot ulcer?"]

    else:
        ans = (
            "Sorry, I don't have an answer for that question yet. "
            "Please consult a healthcare professional for medical advice."
        )

    st.markdown(
        f"""
<div class="answer">
<h3>🤖 AI Response</h3>
<p>{ans}</p>
</div>
""",
        unsafe_allow_html=True
    )

st.markdown("---")

st.info(
    "⚠ This AI Health Assistant provides educational information only and should not replace professional medical advice."
)