import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Birthday Celebration",
    page_icon="🎂",
    layout="centered"
)

# Replace with your deployed Streamlit URL
BASE_URL = "https://birthday-celebrationapp.streamlit.app"

# Query params
params = st.query_params

friend_name = params.get("friend")
sender_name = params.get("sender")
message = params.get("message")

# Global Styling
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
    overflow-x: hidden;
}

/* Remove top spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 900px;
}

/* Animated floating circles */
.floating {
    position: fixed;
    border-radius: 50%;
    opacity: 0.15;
    animation: float 8s infinite ease-in-out;
    z-index: -1;
}

.float1 {
    width: 250px;
    height: 250px;
    background: white;
    top: 10%;
    left: -80px;
}

.float2 {
    width: 180px;
    height: 180px;
    background: white;
    bottom: 10%;
    right: -50px;
    animation-delay: 2s;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-30px);}
    100% {transform: translateY(0px);}
}

/* Glassmorphism card */
.card {
    background: rgba(255,255,255,0.20);
    backdrop-filter: blur(14px);
    border-radius: 30px;
    padding: 40px 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    text-align: center;
    animation: fadeIn 1.2s ease-in-out;
}

/* Fade animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(25px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* Titles */
.big-title {
    font-size: 4rem;
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
    line-height: 1.1;
}

.friend-name {
    font-size: 3rem;
    font-weight: 700;
    color: #fff;
    margin-top: 15px;
    word-wrap: break-word;
}

/* Message */
.message {
    font-size: 1.5rem;
    color: white;
    margin-top: 25px;
    line-height: 1.7;
    word-wrap: break-word;
}

/* Sender */
.sender {
    margin-top: 30px;
    font-size: 1.3rem;
    color: white;
    font-weight: 600;
}

/* Inputs */
.stTextInput input,
.stTextArea textarea {
    border-radius: 15px !important;
    padding: 12px !important;
    border: none !important;
}

/* Button */
.stButton button {
    width: 100%;
    border-radius: 15px;
    padding: 14px;
    background: linear-gradient(90deg,#ff4b4b,#ff6b81);
    color: white;
    border: none;
    font-size: 18px;
    font-weight: 700;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.02);
}

/* Mobile responsiveness */
@media (max-width: 768px) {

    .big-title {
        font-size: 2.5rem;
    }

    .friend-name {
        font-size: 2rem;
    }

    .message {
        font-size: 1.1rem;
    }

    .sender {
        font-size: 1rem;
    }

    .card {
        padding: 25px 18px;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}

</style>

<div class="floating float1"></div>
<div class="floating float2"></div>

""", unsafe_allow_html=True)

# Celebration Page
if friend_name and sender_name and message:

    st.balloons()
    st.snow()

    st.markdown(
        f"""
        <div class="card">

            <div class="big-title">
                🎉 HAPPY BIRTHDAY 🎉
            </div>

            <div class="friend-name">
                🎂 {friend_name}
            </div>

            <div class="message">
                {message}
            </div>

            <div class="sender">
                ❤️ From {sender_name}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# Generator Page
else:

    st.markdown(
        """
        <div class="card">
            <div class="big-title">
                🎂 Birthday Celebration
            </div>

            <div class="message">
                Create beautiful shareable birthday wishes instantly ✨
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    friend_name = st.text_input("🎈 Birthday Person's Name")
    sender_name = st.text_input("❤️ Your Name")

    message = st.text_area(
        "💌 Birthday Wish",
        "Wishing you happiness, success, love, and endless joy on your special day!"
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

        st.success("🎊 Your Celebration Link is Ready!")

        st.code(full_link)

        st.markdown(
            f"""
            <a href="{full_link}" target="_blank">
                <button style="
                    width:100%;
                    padding:16px;
                    border:none;
                    border-radius:15px;
                    background:linear-gradient(90deg,#ff4b4b,#ff6b81);
                    color:white;
                    font-size:18px;
                    font-weight:700;
                    cursor:pointer;
                    margin-top:10px;
                ">
                    🎂 Preview Birthday Page
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )