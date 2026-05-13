import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Birthday Celebration",
    page_icon="🎂",
    layout="centered"
)

# Replace with your actual deployed Streamlit URL
BASE_URL = "https://birthday-celebrationapp.streamlit.app"

# Read query parameters
params = st.query_params

friend_name = params.get("friend")
sender_name = params.get("sender")
message = params.get("message")

# -------------------------
# MOBILE RESPONSIVE STYLES
# -------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Arial', sans-serif;
}

/* Main container */
.main-container {
    width: 100%;
    max-width: 700px;
    margin: auto;
    padding: 10px;
}

/* Birthday card */
.birthday-card {
    background: linear-gradient(135deg, #ff4b6e, #ff8e53);
    padding: 30px 20px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
    margin-top: 30px;
}

/* Title */
.birthday-title {
    font-size: 52px;
    font-weight: 800;
    color: white;
    line-height: 1.2;
}

/* Friend Name */
.birthday-name {
    font-size: 42px;
    font-weight: bold;
    color: white;
    margin-top: 15px;
}

/* Message */
.birthday-message {
    font-size: 24px;
    color: white;
    margin-top: 25px;
    line-height: 1.6;
    word-wrap: break-word;
}

/* Sender */
.birthday-from {
    font-size: 22px;
    color: #fff7f7;
    margin-top: 30px;
    font-weight: 600;
}

/* Mobile Responsive */
@media (max-width: 768px) {

    .birthday-card {
        padding: 25px 18px;
        border-radius: 20px;
    }

    .birthday-title {
        font-size: 34px;
    }

    .birthday-name {
        font-size: 30px;
    }

    .birthday-message {
        font-size: 20px;
    }

    .birthday-from {
        font-size: 18px;
    }
}

/* Input styling */
.stTextInput input,
.stTextArea textarea {
    border-radius: 12px !important;
    font-size: 18px !important;
}

/* Button styling */
.stButton > button {
    width: 100%;
    background-color: #ff4b6e;
    color: white;
    border-radius: 12px;
    height: 3.2em;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

/* Code block */
pre {
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# BIRTHDAY DISPLAY PAGE
# -------------------------

if friend_name and sender_name and message:

    st.balloons()
    st.snow()

    st.markdown(
        f"""
        <div class="main-container">

            <div class="birthday-card">

                <div class="birthday-title">
                    🎆 HAPPY BIRTHDAY 🎆
                </div>

                <div class="birthday-name">
                    🎂 {friend_name}
                </div>

                <div class="birthday-message">
                    "{message}"
                </div>

                <div class="birthday-from">
                    ❤️ From {sender_name}
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# GENERATOR PAGE
# -------------------------

else:

    st.title("🎉 Birthday Celebration Generator")

    st.markdown(
        "Create a personalized birthday celebration link and share it instantly."
    )

    friend_name = st.text_input(
        "🎂 Birthday Person's Name"
    )

    sender_name = st.text_input(
        "❤️ Your Name"
    )

    message = st.text_area(
        "💌 Birthday Wish",
        "Wishing you happiness, success, laughter, and endless joy on your special day!"
    )

    if st.button("🎉 Generate Birthday Link"):

        encoded_friend = urllib.parse.quote(friend_name)
        encoded_sender = urllib.parse.quote(sender_name)
        encoded_message = urllib.parse.quote(message)

        full_link = (
            f"{BASE_URL}/"
            f"?friend={encoded_friend}"
            f"&sender={encoded_sender}"
            f"&message={encoded_message}"
        )

        st.success("✅ Your Shareable Birthday Link is Ready!")

        st.code(full_link)

        st.markdown(
            f"""
            <a href="{full_link}" target="_blank">
                <button style="
                    width:100%;
                    background:#ff4b6e;
                    color:white;
                    border:none;
                    padding:14px;
                    border-radius:12px;
                    font-size:18px;
                    font-weight:bold;
                    cursor:pointer;
                    margin-top:10px;
                ">
                    🎂 Preview Birthday Page
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )