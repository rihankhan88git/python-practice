import streamlit as st
import pickle


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Spam Email Detector",
    page_icon="📧",
    layout="wide"
)


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    }

    .spam-box {
        background-color: #ffe6e6;
        border: 2px solid #ff4d4d;
    }

    .ham-box {
        background-color: #e6ffe6;
        border: 2px solid #33cc33;
    }

    .result-title {
        font-size: 32px;
        font-weight: bold;
    }

    .probability {
        font-size: 22px;
        font-weight: bold;
        margin-top: 10px;
    }

    .info-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #dddddd;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():

    with open("spam_model.pkl", "rb") as file:

        model_data = pickle.load(file)

    model = model_data["model"]
    vectorizer = model_data["vectorizer"]

    return model, vectorizer


# ==========================================================
# TRY TO LOAD MODEL
# ==========================================================

try:

    model, vectorizer = load_model()

except FileNotFoundError:

    st.error(
        "❌ spam_model.pkl not found!"
    )

    st.info(
        "Please run main.py first to train and save the model."
    )

    st.stop()


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<div class="main-title">📧 AI Spam Email Detector</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning based Spam Detection using TF-IDF + Logistic Regression</div>',
    unsafe_allow_html=True
)

st.divider()


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("⚙️ Model Information")

    st.write("*Algorithm:*")
    st.write("Logistic Regression")

    st.write("*Text Processing:*")
    st.write("TF-IDF Vectorization")

    st.write("*Problem Type:*")
    st.write("Binary Classification")

    st.write("*Classes:*")
    st.write("📧 Ham / Spam")

    st.divider()

    st.header("📚 How it works")

    st.write(
        """
        1. User enters an email/message
        2. Text is converted using TF-IDF
        3. Logistic Regression analyzes the text
        4. Model predicts Spam or Ham
        5. Spam probability is displayed
        """
    )


# ==========================================================
# MAIN UI
# ==========================================================

st.subheader("📨 Enter Email / Message")

email_text = st.text_area(
    "Type or paste your message below:",
    height=220,
    placeholder=(
        "Example:\n\n"
        "Congratulations! You have won a free prize. "
        "Click here to claim your reward."
    )
)


# ==========================================================
# BUTTON
# ==========================================================

predict_button = st.button(
    "🔍 Check Message",
    type="primary",
    use_container_width=True
)


# ==========================================================
# PREDICTION
# ==========================================================

if predict_button:

    if email_text.strip() == "":

        st.warning(
            "⚠️ Please enter an email or message first."
        )

    else:

        # --------------------------------------------------
        # Convert text into TF-IDF
        # --------------------------------------------------

        text_vector = vectorizer.transform(
            [email_text]
        )

        # --------------------------------------------------
        # Prediction
        # --------------------------------------------------

        prediction = model.predict(
            text_vector
        )[0]

        # --------------------------------------------------
        # Probability
        # --------------------------------------------------

        probabilities = model.predict_proba(
            text_vector
        )[0]

        classes = list(model.classes_)

        spam_index = classes.index("spam")
        ham_index = classes.index("ham")

        spam_probability = probabilities[spam_index]
        ham_probability = probabilities[ham_index]


        # ==================================================
        # SPAM RESULT
        # ==================================================

        if prediction == "spam":

            st.markdown(
                f"""
                <div class="result-box spam-box">

                    <div class="result-title">
                        🚨 SPAM DETECTED
                    </div>

                    <div class="probability">
                        Spam Probability:
                        {spam_probability * 100:.2f}%
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        # ==================================================
        # HAM RESULT
        # ==================================================

        else:

            st.markdown(
                f"""
                <div class="result-box ham-box">

                    <div class="result-title">
                        ✅ NOT SPAM
                    </div>

                    <div class="probability">
                        Ham Probability:
                        {ham_probability * 100:.2f}%
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ==================================================
        # PROBABILITY SECTION
        # ==================================================

        st.subheader("📊 Prediction Probability")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "📧 Ham Probability",
                f"{ham_probability * 100:.2f}%"
            )

            st.progress(
                float(ham_probability)
            )

        with col2:

            st.metric(
                "🚨 Spam Probability",
                f"{spam_probability * 100:.2f}%"
            )

            st.progress(
                float(spam_probability)
            )


        # ==================================================
        # MODEL DECISION
        # ==================================================

        st.subheader("🤖 Model Decision")

        if prediction == "spam":

            st.error(
                "The Machine Learning model classified this "
                "message as SPAM."
            )

        else:

            st.success(
                "The Machine Learning model classified this "
                "message as NOT SPAM (HAM)."
            )


# ==========================================================
# EXAMPLE MESSAGES
# ==========================================================

st.divider()

st.subheader("🧪 Try Example Messages")

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        ### 🚨 Spam Example

        *"Congratulations! You have won a free cash prize. Click now to claim your reward."*
        """
    )

with col2:

    st.markdown(
        """
        ### ✅ Normal Example

        *"Please send me the project report before lunch."*
        """
    )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center;">

    <b>AI Spam Email Detector</b><br>

    Built with Python • Pandas • Scikit-learn • TF-IDF • Logistic Regression • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)