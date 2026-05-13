import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Birthday Celebration",
    page_icon="🎂",
    layout="centered"
)

# Replace with your deployed Streamlit URL
BASE_URL = "https://birthday-celebrationapp.streamlit.app"

# Read URL query params
params = st.query_params

friend_name = params.get("friend")
sender_name = params.get("sender")
message = params.get("message")

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

/* Hide Streamlit Menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Background */
.stApp {
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
}

/* Flying balloons */
.balloon {
    position: fixed;
    bottom: -150px;
    font-size: 40px;
    animation: floatUp 10s linear infinite;
    opacity: 0.9;
}

.balloon:nth-child(1) {
    left: 10%;
    animation-duration: 9s;
}

.balloon:nth-child(2) {
    left: 30%;
    animation-duration: 12s;
}

.balloon:nth-child(3) {
    left: 50%;
    animation-duration: 10s;
}

.balloon:nth-child(4) {
    left: 70%;
    animation-duration: 11s;
}

.balloon:nth-child(5) {
    left: 90%;
    animation-duration: 13s;
}

@keyframes floatUp {
    0% {
        transform: translateY(0);
        opacity: 0;
    }

    20% {
        opacity: 1;
    }

    100% {
        transform: translateY(-120vh);
        opacity: 0;
    }
}

/* Card */
.birthday-card {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(12px);
    padding: 35px 25px;
    border-radius: 25px;
    text-align: center;
    margin-top: 60px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}

/* Title */
.birthday-title {
    font-size: 52px;
    color: white;
    font-weight: 800;
    line-height: 1.3;
}

/* Name */
.birthday-name {
    font-size: 40px;
    color: white;
    margin-top: 15px;
    font-weight: bold;
}

/* Message */
.birthday-message {
    font-size: 24px;
    color: white;
    margin-top: 25px;
    line-height: 1.7;
}

/* From */
.birthday-from {
    font-size: 22px;
    color: white;
    margin-top: 30px;
    font-weight: 600;
}

/* Inputs */
.stTextInput input,
.stTextArea textarea {
    border-radius: 12px !important;
    font-size: 18px !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background: #ff4b6e;
    color: white;
    border: none;
    border-radius: 12px;
    height: 3.3em;
    font-size: 18px;
    font-weight: bold;
}

/* Mobile */
@media (max-width: 768px) {

    .birthday-card {
        padding: 25px 18px;
    }

    .birthday-title {
        font-size: 34px;
    }

    .birthday-name {
        font-size: 28px;
    }

    .birthday-message {
        font-size: 20px;
    }

    .birthday-from {
        font-size: 18px;
    }

    .balloon {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# SHOW BIRTHDAY PAGE
# -------------------------

if friend_name and sender_name and message:

    st.balloons()

    # Flying balloons HTML
    st.markdown("""
    <div class="balloon">🎈</div>
    <div class="balloon">🎈</div>
    <div class="balloon">🎈</div>
    <div class="balloon">🎈</div>
    <div class="balloon">🎈</div>
    """, unsafe_allow_html=True)

    # Birthday Card
    st.markdown(f"""
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
    """, unsafe_allow_html=True)

# -------------------------
# GENERATOR PAGE
# -------------------------

else:

    st.title("🎉 Birthday Celebration Generator")

    st.write(
        "Create a personalized birthday celebration page and share it instantly."
    )

    friend_name = st.text_input("🎂 Birthday Person's Name")

    sender_name = st.text_input("❤️ Your Name")

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

        st.success("✅ Birthday Link Ready!")

        st.code(full_link)

        st.markdown(f"""
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
                margin-top:10px;
                cursor:pointer;
            ">
                🎂 Preview Birthday Page
            </button>
        </a>
        """, unsafe_allow_html=True)